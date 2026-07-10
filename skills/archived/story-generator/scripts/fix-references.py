#!/usr/bin/env python3
"""
fix-references.py — One-shot legacy-fix tool for replacing PLACEHOLDER URLs
in a story's References section with real, working links.

When to use this
----------------
New stories generated with this skill should already have real URLs in the
References section (see SKILL.md section "References Guidance"). This script
exists only for legacy cleanup — stories that were generated before the skill
update and still contain `(PLACEHOLDER)` placeholder URLs.

Per the skill convention, each story gets 5 references:
  1. Wikipedia biography of the subject
  2. Wikipedia article on the subject's main contribution
  3. Wikipedia article on a related concept or work
  4. MacTutor History of Mathematics / Nobel Prize / NASA / institutional bio
  5. Encyclopedia Britannica / Stanford Encyclopedia of Philosophy

How to use
----------
1. Copy this script to your project: e.g., `cp /path/to/this.py src/stories/`
2. Edit the REFS dict below to list every story that needs updating.
   Each entry is: story-dir-name -> list of (title, url, description) tuples.
3. Run: python3 fix-references.py
4. The script rewrites everything from the "## References" heading to EOF
   in each listed story's index.md. Safe to re-run.

This script is intentionally NOT generic or automated — curating good
references is a judgment call. Maintaining a project-local customized copy
with a hand-picked REFS dict is the right approach.

Example skeleton (replace with your own stories):
"""
from pathlib import Path

# Fill this dict with one entry per story that needs legacy cleanup.
# Each list must contain 5 tuples: (title, url, one-line description).
# First 3 entries should be Wikipedia URLs per skill convention.
REFS = {
    # "example-scientist": [
    #     ("Wikipedia: Example Scientist",
    #      "https://en.wikipedia.org/wiki/Example_Scientist",
    #      "Biography of the example scientist"),
    #     ("Wikipedia: Example Contribution",
    #      "https://en.wikipedia.org/wiki/Example_Contribution",
    #      "The scientist's main discovery"),
    #     ("Wikipedia: Example Related Concept",
    #      "https://en.wikipedia.org/wiki/Example_Related_Concept",
    #      "A related topic or work"),
    #     ("MacTutor: Example Scientist",
    #      "https://mathshistory.st-andrews.ac.uk/Biographies/Example/",
    #      "University of St Andrews history of mathematics archive"),
    #     ("Encyclopaedia Britannica: Example Scientist",
    #      "https://www.britannica.com/biography/Example-Scientist",
    #      "Overview of the scientist's life and contributions"),
    # ],
}


def rewrite_references(index_md: Path, refs: list) -> bool:
    """
    Replace everything from '## References' to EOF in index_md with a new
    block built from the provided refs list. Returns True if the heading
    was found and the file was rewritten.
    """
    text = index_md.read_text(encoding="utf-8")
    marker = "## References"
    idx = text.find(marker)
    if idx == -1:
        print(f"  WARNING: no '{marker}' heading in {index_md}")
        return False

    preserve = text[:idx].rstrip() + "\n\n"
    new_block = f"{marker}\n\n"
    for i, (title, url, desc) in enumerate(refs, start=1):
        new_block += f"{i}. [{title}]({url}) - {desc}\n"

    index_md.write_text(preserve + new_block, encoding="utf-8")
    return True


def main():
    if not REFS:
        print("REFS dict is empty. Edit this script to list stories that need "
              "legacy-placeholder cleanup, then re-run.")
        return

    stories_root = Path("docs/stories")
    ok, missing = 0, 0
    for story_name, refs in REFS.items():
        index_md = stories_root / story_name / "index.md"
        if not index_md.exists():
            print(f"SKIP (no index.md): {index_md}")
            missing += 1
            continue
        if len(refs) != 5:
            print(f"WARNING: {story_name} has {len(refs)} refs, expected 5")
        if rewrite_references(index_md, refs):
            print(f"updated: {index_md}")
            ok += 1

    print(f"\nDone. {ok} files updated, {missing} missing.")


if __name__ == "__main__":
    main()
