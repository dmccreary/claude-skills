#!/usr/bin/env python3
"""
generate-images.py — Generate graphic novel panel images for a story using
Google Gemini 2.5 Flash Image (aka "Nano Banana") with an explicit
aspect_ratio so the model returns landscape images natively.

Why this script exists
----------------------
Many AI agents expose a generic `generate_image` tool that does not let the
caller pick an aspect ratio. The default is almost always 1:1 (square),
which means graphic novel panels come back as squares and must be
lossy-cropped to 16:9 afterward, destroying ~44% of the vertical content.

This script calls Gemini directly via the google-genai SDK and passes:

    image_config=types.ImageConfig(aspect_ratio="16:9")

so the model returns a 16:9 image natively (1344x768 at the current model
resolution). No post-processing required.

Reference (official):
  https://developers.googleblog.com/gemini-2-5-flash-image-now-ready-for-production-with-new-aspect-ratios/

Usage
-----
    # Generate every image referenced in a story index.md
    python generate-images.py docs/stories/rene-descartes

    # Just the first (cover) image — verifies aspect ratio and style on one
    # image before committing API credits to the remaining 12 panels
    python generate-images.py docs/stories/rene-descartes --first-only

    # Resume after a partial run
    python generate-images.py docs/stories/rene-descartes --skip-existing

    # Portrait aspect for a book cover
    python generate-images.py docs/stories/rene-descartes --aspect-ratio 2:3

Environment
-----------
    export GEMINI_API_KEY=...    (or GOOGLE_API_KEY)

Get a free API key at https://aistudio.google.com/apikey. The free tier
allows 500 requests per day and 10 requests per minute, which comfortably
covers two full 208-image textbooks per day at zero cost.

Requires: pip install google-genai
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from google import genai
from google.genai import types

# Gemini 2.5 Flash Image paid-tier pricing (USD) as of early 2026.
# Source: https://ai.google.dev/gemini-api/docs/pricing
PRICE_INPUT_PER_1M = 0.30    # text input tokens
PRICE_OUTPUT_PER_1M = 30.00  # image output tokens

# Free-tier rate limit for gemini-2.5-flash-image. 10 RPM => one request
# every 6 seconds at minimum. The script enforces this client-side so it
# never trips a 429. Override with --rpm if you're on the paid tier with a
# higher quota.
# Source: https://ai.google.dev/gemini-api/docs/rate-limits
DEFAULT_RPM_LIMIT = 10

# Supported aspect ratios from the Gemini 2.5 Flash Image production release.
# Source: https://developers.googleblog.com/gemini-2-5-flash-image-now-ready-for-production-with-new-aspect-ratios/
SUPPORTED_ASPECT_RATIOS = {
    "21:9", "16:9", "4:3", "3:2", "1:1",
    "9:16", "3:4", "2:3", "5:4", "4:5",
}

# Machine-readable audit log: one JSONL record per successful image.
# Hardcoded to logs/ at the project root per skill convention.
USAGE_LOG = Path("logs/image-generation-usage.jsonl")


class RateLimiter:
    """
    Enforces a minimum interval between API calls so we stay under the
    Gemini free-tier 10 RPM cap. Uses wall-clock time, not a sliding window,
    which is simpler and strictly more conservative. Also tracks total
    cumulative sleep time for end-of-run reporting.
    """
    def __init__(self, rpm: int):
        self.min_interval = 60.0 / rpm if rpm > 0 else 0.0
        self.last_request_time: float | None = None
        self.total_sleep_sec: float = 0.0

    def wait(self) -> None:
        if self.last_request_time is None or self.min_interval <= 0:
            self.last_request_time = time.monotonic()
            return
        elapsed = time.monotonic() - self.last_request_time
        remaining = self.min_interval - elapsed
        if remaining > 0:
            print(f"   rate-limit: sleeping {remaining:.1f}s to stay under "
                  f"{60 / self.min_interval:.0f} RPM")
            time.sleep(remaining)
            self.total_sleep_sec += remaining
        self.last_request_time = time.monotonic()


# Match <details><summary>...Prompt...</summary>BODY</details> blocks.
_PROMPT_BLOCK = re.compile(
    r"<details>\s*<summary>([^<]*?Prompt[^<]*?)</summary>\s*(.*?)\s*</details>",
    re.DOTALL,
)


def parse_aspect_ratio(value: str) -> float:
    """Convert '16:9' → 1.7778. Raises ValueError on bad input."""
    try:
        w, h = value.split(":")
        return int(w) / int(h)
    except Exception as e:
        raise ValueError(f"bad aspect ratio {value!r}: expected 'W:H'") from e


def extract_prompts(index_md: Path):
    """
    Parse a story index.md and return a list of (output_path, prompt_text)
    tuples in document order: cover image first, then panel-01, panel-02, ...
    """
    text = index_md.read_text(encoding="utf-8")
    story_dir = index_md.parent

    blocks = [
        m for m in _PROMPT_BLOCK.finditer(text) if "Image Prompt" in m.group(1)
    ]
    if not blocks:
        return []

    prompts = [(story_dir / "cover.png", blocks[0].group(2).strip())]
    for i, m in enumerate(blocks[1:], start=1):
        prompts.append((story_dir / f"panel-{i:02d}.png", m.group(2).strip()))
    return prompts


def log_usage(out_path: Path, response, aspect_ratio: str) -> dict:
    """
    Extract usage_metadata from the API response, estimate the paid-tier cost,
    and append one JSON line to logs/image-generation-usage.jsonl. Returns the
    record dict so the caller can print a summary.
    """
    um = getattr(response, "usage_metadata", None)
    input_tokens = getattr(um, "prompt_token_count", 0) or 0
    output_tokens = getattr(um, "candidates_token_count", 0) or 0
    total_tokens = getattr(um, "total_token_count", 0) or (input_tokens + output_tokens)

    cost_usd = (
        input_tokens * PRICE_INPUT_PER_1M / 1_000_000
        + output_tokens * PRICE_OUTPUT_PER_1M / 1_000_000
    )

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "file": str(out_path),
        "model": "gemini-2.5-flash-image",
        "aspect_ratio": aspect_ratio,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "paid_tier_cost_usd": round(cost_usd, 6),
    }

    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with USAGE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    return record


def generate_one(client: genai.Client, prompt: str, out_path: Path,
                 limiter: RateLimiter, aspect_ratio: str) -> tuple[bool, dict | None]:
    """
    Call Gemini 2.5 Flash Image with the requested aspect_ratio and write the
    first returned image to out_path. Returns (success, record) where record
    is a dict of metadata captured during the call (tokens, cost, wall-clock
    time, byte size). Respects the provided RateLimiter before the API call.
    """
    print(f"-> generating {out_path}")
    limiter.wait()
    t0 = time.monotonic()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
            ),
        )
    except Exception as e:
        print(f"   ERROR: API call failed: {type(e).__name__}: {e}")
        return False, None
    wall_clock_sec = time.monotonic() - t0

    # Gemini sometimes returns a candidate with no content (safety filter,
    # refusal, or empty response). Handle all of these gracefully.
    candidates = getattr(response, "candidates", None) or []
    if not candidates:
        print(f"   ERROR: response has no candidates (likely blocked by safety filter)")
        prompt_feedback = getattr(response, "prompt_feedback", None)
        if prompt_feedback:
            print(f"   prompt_feedback: {prompt_feedback}")
        return False, None

    candidate = candidates[0]
    finish_reason = getattr(candidate, "finish_reason", None)
    content = getattr(candidate, "content", None)
    if content is None:
        print(f"   ERROR: candidate has no content "
              f"(finish_reason={finish_reason}) — likely safety filter")
        safety = getattr(candidate, "safety_ratings", None)
        if safety:
            print(f"   safety_ratings: {safety}")
        return False, None

    parts = getattr(content, "parts", None) or []
    for part in parts:
        inline = getattr(part, "inline_data", None)
        if inline and inline.data:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(inline.data)
            file_size = out_path.stat().st_size
            print(f"   wrote {out_path} ({file_size:,} bytes, "
                  f"{wall_clock_sec:.1f}s wall-clock)")
            rec = log_usage(out_path, response, aspect_ratio)
            rec["wall_clock_sec"] = round(wall_clock_sec, 2)
            rec["file_size_bytes"] = file_size
            rec["prompt_excerpt"] = " ".join(prompt.split())[:160]
            print(
                f"   tokens in/out: {rec['input_tokens']}/{rec['output_tokens']}  "
                f"paid-tier cost: ${rec['paid_tier_cost_usd']:.4f}  "
                f"(free on the free tier)"
            )
            return True, rec

    print(f"   ERROR: no image data returned")
    for part in parts:
        if getattr(part, "text", None):
            print(f"   text part: {part.text[:300]}")
    return False, None


def write_story_log(
    story_dir: Path,
    index_md: Path,
    records: list[dict],
    run_started_at: datetime,
    run_finished_at: datetime,
    rpm_limit: int,
    limiter_sleep_sec: float,
    aspect_ratio: str,
    args_first_only: bool,
    args_skip_existing: bool,
) -> Path:
    """
    Write a per-story markdown log to logs/{story-name}-{YYYY-MM-DD}.md
    containing all metadata captured during this run. Overwrites any prior
    log for the same story on the same day.
    """
    story_name = story_dir.name
    date_str = run_started_at.astimezone().strftime("%Y-%m-%d")
    log_path = Path("logs") / f"{story_name}-{date_str}.md"

    total_images = len(records)
    total_input = sum(r["input_tokens"] for r in records)
    total_output = sum(r["output_tokens"] for r in records)
    total_tokens = sum(r["total_tokens"] for r in records)
    total_cost = sum(r["paid_tier_cost_usd"] for r in records)
    total_bytes = sum(r.get("file_size_bytes", 0) for r in records)
    total_wall = sum(r.get("wall_clock_sec", 0.0) for r in records)
    run_duration = (run_finished_at - run_started_at).total_seconds()

    flags = []
    if args_first_only:
        flags.append("`--first-only`")
    if args_skip_existing:
        flags.append("`--skip-existing`")
    flags_str = " ".join(flags) if flags else "(none)"

    lines: list[str] = []
    lines.append(f"# Image Generation Log: {story_name}")
    lines.append("")
    lines.append(f"**Run date:** {date_str}  ")
    lines.append(f"**Run started:** {run_started_at.astimezone().isoformat(timespec='seconds')}  ")
    lines.append(f"**Run finished:** {run_finished_at.astimezone().isoformat(timespec='seconds')}  ")
    lines.append(f"**Total wall-clock:** {run_duration:.1f} seconds "
                 f"({run_duration/60:.1f} minutes)  ")
    lines.append(f"**Story directory:** `{story_dir}`  ")
    lines.append(f"**Source index:** `{index_md}`  ")
    lines.append(f"**Model:** `gemini-2.5-flash-image`  ")
    lines.append(f"**Aspect ratio:** `{aspect_ratio}` (native, no post-processing)  ")
    lines.append(f"**Rate limit:** {rpm_limit} RPM  ")
    lines.append(f"**Rate-limiter total sleep:** {limiter_sleep_sec:.1f} seconds  ")
    lines.append(f"**CLI flags:** {flags_str}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Images generated:** {total_images}")
    lines.append(f"- **Total input tokens:** {total_input:,}")
    lines.append(f"- **Total output tokens:** {total_output:,}")
    lines.append(f"- **Total tokens:** {total_tokens:,}")
    lines.append(f"- **Total PNG payload:** {total_bytes:,} bytes "
                 f"({total_bytes/1024/1024:.2f} MB)")
    lines.append(f"- **Sum of per-image wall-clock:** {total_wall:.1f} seconds")
    lines.append(f"- **Paid-tier cost:** ${total_cost:.4f}")
    lines.append(f"- **Free-tier quota used:** {total_images}/500 "
                 f"({total_images/500*100:.1f}% of one day)")
    lines.append(f"- **Actual cost on free tier:** $0.00")
    lines.append("")
    lines.append("## Per-Image Details")
    lines.append("")
    lines.append("| # | File | Dimensions | Size (bytes) | Tokens in | Tokens out | Total tokens | Wall-clock (s) | Paid cost (USD) |")
    lines.append("|---|------|------------|--------------|-----------|------------|--------------|----------------|-----------------|")
    for i, r in enumerate(records, 1):
        fname = Path(r["file"]).name
        dims = r.get("dimensions", "—")
        size = r.get("file_size_bytes", 0)
        lines.append(
            f"| {i} "
            f"| `{fname}` "
            f"| {dims} "
            f"| {size:,} "
            f"| {r['input_tokens']} "
            f"| {r['output_tokens']} "
            f"| {r['total_tokens']} "
            f"| {r.get('wall_clock_sec', 0):.1f} "
            f"| ${r['paid_tier_cost_usd']:.4f} |"
        )
    lines.append("")
    lines.append("## Prompt Excerpts")
    lines.append("")
    lines.append("First ~160 characters of each prompt, for provenance:")
    lines.append("")
    for i, r in enumerate(records, 1):
        fname = Path(r["file"]).name
        excerpt = r.get("prompt_excerpt", "").replace("|", "\\|")
        lines.append(f"{i}. **`{fname}`** — {excerpt}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Token counts and costs come directly from "
                 "`response.usage_metadata` on each API response.")
    lines.append(f"- All images returned at native {aspect_ratio} via "
                 f"`types.ImageConfig(aspect_ratio=\"{aspect_ratio}\")`. No post-processing.")
    lines.append("- Free-tier rate limits: 10 RPM, 500 RPD, "
                 "~250,000 TPM. This run used "
                 f"{total_images} of 500 daily requests.")
    lines.append("- The machine-readable JSONL equivalent of this log lives "
                 "at `logs/image-generation-usage.jsonl`.")
    lines.append("")

    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(lines), encoding="utf-8")
    return log_path


def verify_dimensions(path: Path):
    """Return (width, height) using `sips` on macOS, or None on failure."""
    try:
        out = subprocess.check_output(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
            text=True,
        )
        w = int(re.search(r"pixelWidth:\s*(\d+)", out).group(1))
        h = int(re.search(r"pixelHeight:\s*(\d+)", out).group(1))
        return w, h
    except Exception as e:
        print(f"   verify_dimensions failed: {e}")
        return None


def matches_aspect(w: int, h: int, target_ratio: float, tolerance: float = 0.03) -> bool:
    return abs((w / h) - target_ratio) / target_ratio < tolerance


def _finalize_run(story_dir, index_md, run_records, run_started_at, args, limiter):
    """Write the per-story markdown log. Safe to call on partial runs."""
    if not run_records:
        return
    log_path = write_story_log(
        story_dir=story_dir,
        index_md=index_md,
        records=run_records,
        run_started_at=run_started_at,
        run_finished_at=datetime.now(timezone.utc),
        rpm_limit=args.rpm,
        limiter_sleep_sec=limiter.total_sleep_sec,
        aspect_ratio=args.aspect_ratio,
        args_first_only=args.first_only,
        args_skip_existing=args.skip_existing,
    )
    print(f"\nPer-story log written: {log_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("story_dir", help="Path to story directory containing index.md")
    ap.add_argument("--first-only", action="store_true",
                    help="Only generate the first (cover) image for testing")
    ap.add_argument("--skip-existing", action="store_true",
                    help="Skip images whose output file already exists")
    ap.add_argument("--rpm", type=int, default=DEFAULT_RPM_LIMIT,
                    help="Max requests per minute (default: 10, the free-tier cap). "
                         "Set higher on the paid tier, or 0 to disable throttling.")
    ap.add_argument("--aspect-ratio", default="16:9",
                    choices=sorted(SUPPORTED_ASPECT_RATIOS),
                    help="Image aspect ratio passed to Gemini ImageConfig. "
                         "Default: 16:9. For book covers or portrait illustrations, "
                         "use 2:3 or 3:4. For extra-wide cinematic panels, use 21:9.")
    args = ap.parse_args()

    story_dir = Path(args.story_dir)
    index_md = story_dir / "index.md"
    if not index_md.exists():
        sys.exit(f"ERROR: {index_md} not found")

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("ERROR: set GEMINI_API_KEY (or GOOGLE_API_KEY) in your environment. "
                 "Get a free key at https://aistudio.google.com/apikey")

    target_ratio = parse_aspect_ratio(args.aspect_ratio)

    client = genai.Client(api_key=api_key)
    limiter = RateLimiter(args.rpm)
    run_started_at = datetime.now(timezone.utc)
    run_records: list[dict] = []

    prompts = extract_prompts(index_md)
    if not prompts:
        sys.exit(f"ERROR: no image prompts found in {index_md}")

    print(f"Found {len(prompts)} image prompts in {index_md}")
    print(f"Aspect ratio: {args.aspect_ratio}  |  Rate limit: {args.rpm} RPM")
    if args.first_only:
        prompts = prompts[:1]
        print("--first-only: generating only the cover image for verification\n")
    else:
        print()

    for out_path, prompt in prompts:
        if args.skip_existing and out_path.exists():
            print(f"-> skipping {out_path} (already exists)\n")
            continue
        ok, rec = generate_one(client, prompt, out_path, limiter, args.aspect_ratio)
        if not ok or rec is None:
            print(f"   SKIPPING {out_path} — will continue with next image\n")
            continue
        dims = verify_dimensions(out_path)
        if dims:
            w, h = dims
            tag = f"OK {args.aspect_ratio}" if matches_aspect(w, h, target_ratio) \
                else f"NOT {args.aspect_ratio}"
            print(f"   dimensions: {w}x{h}  [{tag}]")
            rec["dimensions"] = f"{w}x{h}"
            if not matches_aspect(w, h, target_ratio):
                run_records.append(rec)
                _finalize_run(story_dir, index_md, run_records,
                              run_started_at, args, limiter)
                sys.exit(f"ABORT: {out_path} does not match {args.aspect_ratio} — "
                         f"check ImageConfig")
        run_records.append(rec)
        print()

    _finalize_run(story_dir, index_md, run_records, run_started_at, args, limiter)

    # Per-run cost summary from today's appended records
    if USAGE_LOG.exists():
        today = datetime.now(timezone.utc).date().isoformat()
        today_records = []
        for line in USAGE_LOG.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
                if r.get("timestamp", "").startswith(today):
                    today_records.append(r)
            except json.JSONDecodeError:
                pass
        if today_records:
            total_cost = sum(r["paid_tier_cost_usd"] for r in today_records)
            total_tokens = sum(r["total_tokens"] for r in today_records)
            print(f"\nToday: {len(today_records)} images, "
                  f"{total_tokens:,} total tokens, "
                  f"${total_cost:.4f} paid-tier cost "
                  f"(free tier: {len(today_records)}/500 requests used)")

    print("Done.")


if __name__ == "__main__":
    main()
