#!/usr/bin/env python3
"""
README Validation Script

Validates README.md files for:
- Required sections present
- Working links (basic check)
- Valid badge URLs
- Proper markdown formatting
- Common issues

Usage:
    python validate-readme.py [path/to/README.md]

Output:
    Validation report with score and recommendations
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse


AUTHORITY_SCRIPT = Path(__file__).with_name("license_authority.py")
AUTHORITY_SPEC = importlib.util.spec_from_file_location(
    "book_publisher_license_authority", AUTHORITY_SCRIPT
)
license_authority = importlib.util.module_from_spec(AUTHORITY_SPEC)
assert AUTHORITY_SPEC.loader is not None
AUTHORITY_SPEC.loader.exec_module(license_authority)

def check_required_sections(
    content: str,
) -> Tuple[List[str], List[str], List[str], List[str]]:
    """Check for required README sections."""
    required = [
        'overview',
        'getting started',
        'contact'
    ]

    recommended = [
        'installation',
        'usage',
        'contributing',
        'acknowledgements',
        'issues',
        'license'
    ]

    found_required = []
    found_recommended = []
    missing_required = []
    missing_recommended = []

    section_headings = extract_section_headings(content)

    for section in required:
        if section in section_headings:
            found_required.append(section)
        else:
            missing_required.append(section)

    for section in recommended:
        if section in section_headings:
            found_recommended.append(section)
        else:
            missing_recommended.append(section)

    return (found_required, missing_required, found_recommended, missing_recommended)


def normalize_section_heading(heading: str) -> str:
    """Normalize a Markdown heading for exact section-name matching."""
    heading = re.sub(r"\s+#+\s*$", "", heading.strip())
    return re.sub(r"[-_\s]+", " ", heading).strip().lower()


def extract_section_headings(content: str) -> set[str]:
    """Extract ATX and Setext headings without matching ordinary prose."""
    headings: set[str] = set()
    lines = content.splitlines()

    for index, line in enumerate(lines):
        atx_match = re.match(r"^[ \t]{0,3}#{1,6}[ \t]+(.+?)\s*$", line)
        if atx_match:
            headings.add(normalize_section_heading(atx_match.group(1)))
            continue

        if index == 0 or not line.strip():
            continue
        if re.match(r"^[ \t]{0,3}(?:=+|-+)[ \t]*$", line):
            headings.add(normalize_section_heading(lines[index - 1]))

    return headings

def extract_links(content: str) -> List[Tuple[str, str]]:
    """Extract all markdown links from content."""
    # Match [text](url) format
    links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
    return links

def validate_url_format(url: str) -> bool:
    """Validate URL format (basic check)."""
    try:
        candidate = url.strip()
        if not candidate or re.search(r"[\x00-\x20]", candidate):
            return False
        result = urlparse(candidate)
        if result.scheme:
            return result.scheme in {"http", "https", "mailto"}
        # Markdown destinations commonly use bare repository-relative paths.
        return bool(result.path or result.fragment or result.query)
    except ValueError:
        return False

def extract_badges(content: str) -> List[str]:
    """Extract badge URLs from content."""
    badges = []
    # Find badge patterns like [![...](badge-url)](link-url)
    badge_pattern = r'\[!\[([^\]]*)\]\(([^\)]+)\)\]\(([^\)]+)\)'
    matches = re.findall(badge_pattern, content)
    for match in matches:
        badges.append(match[1])  # badge URL
    return badges


def extract_claimed_license_ids(
    content: str,
    allow_bare_identifiers: bool = False,
) -> List[str]:
    """Extract common license names that the README affirmatively claims."""
    patterns = {
        "MIT": r"\bmit license\b|license[- :]+mit\b",
        "Apache-2.0": r"\bapache(?: license)?(?:[- ]+version)?[- ]*2\.0\b",
        "GPL-3.0": r"\b(?:gnu general public license|gpl)(?:[- v]+)3(?:\.0)?\b",
        "CC-BY-NC-SA-4.0": (
            r"\bcc[- ]by[- ]nc[- ]sa[- ]4\.0\b|"
            r"creative commons attribution-noncommercial-sharealike 4\.0"
        ),
        "CC-BY-NC-4.0": (
            r"\bcc[- ]by[- ]nc[- ]4\.0\b|"
            r"creative commons attribution-noncommercial 4\.0"
        ),
        "CC-BY-SA-4.0": (
            r"\bcc[- ]by[- ]sa[- ]4\.0\b|"
            r"creative commons attribution-sharealike 4\.0"
        ),
        "CC-BY-4.0": (
            r"\bcc[- ]by[- ]4\.0\b|creative commons attribution 4\.0"
        ),
    }
    if allow_bare_identifiers:
        bare_patterns = {
            "MIT": r"\bmit\b",
            "Apache-2.0": r"\bapache[- ]2\.0\b",
            "GPL-3.0": r"\bgpl[- v]?3(?:\.0)?\b",
            "CC-BY-NC-SA-4.0": r"\bcc[- ]by[- ]nc[- ]sa[- ]4\.0\b",
            "CC-BY-NC-4.0": r"\bcc[- ]by[- ]nc[- ]4\.0\b",
            "CC-BY-SA-4.0": r"\bcc[- ]by[- ]sa[- ]4\.0\b",
            "CC-BY-4.0": r"\bcc[- ]by[- ]4\.0\b",
        }
        patterns = {
            license_id: f"(?:{pattern})|(?:{bare_patterns[license_id]})"
            for license_id, pattern in patterns.items()
        }

    return [
        license_id
        for license_id, pattern in patterns.items()
        if re.search(pattern, content, flags=re.IGNORECASE)
    ]


def extract_named_section(content: str, section_name: str) -> str:
    """Return one Markdown section body, stopping at its next peer heading."""
    lines = content.splitlines()
    start_index: Optional[int] = None
    section_level = 0

    for index, line in enumerate(lines):
        atx_match = re.match(r"^[ \t]{0,3}(#{1,6})[ \t]+(.+?)\s*$", line)
        setext_match = index > 0 and bool(
            re.match(r"^[ \t]{0,3}(?:=+|-+)[ \t]*$", line)
        )
        if atx_match:
            level = len(atx_match.group(1))
            heading = normalize_section_heading(atx_match.group(2))
            content_start = index + 1
        elif setext_match and lines[index - 1].strip():
            level = 1 if line.lstrip().startswith("=") else 2
            heading = normalize_section_heading(lines[index - 1])
            content_start = index + 1
        else:
            continue
        if start_index is None:
            if heading == section_name:
                start_index = content_start
                section_level = level
            continue
        if level <= section_level:
            boundary = index - 1 if setext_match else index
            return "\n".join(lines[start_index:boundary])

    if start_index is None:
        return ""
    return "\n".join(lines[start_index:])


def check_license_authority(
    content: str,
    repo_root: Path,
    authorized_license: Optional[str] = None,
) -> Dict[str, object]:
    """Validate README license claims against repository evidence."""
    authority = license_authority.inspect_repository(
        repo_root,
        authorized_license=authorized_license,
    )
    headings = extract_section_headings(content)
    has_section = "license" in headings
    claimed_ids = extract_claimed_license_ids(content)
    if has_section:
        section_claims = extract_claimed_license_ids(
            extract_named_section(content, "license"),
            allow_bare_identifiers=True,
        )
        claimed_ids = list(dict.fromkeys([*claimed_ids, *section_claims]))
    badge_matches = re.findall(
        r"\[!\[([^\]]*)\]\(([^\)]+)\)\]\(([^\)]+)\)",
        content,
    )
    has_badge = any(
        re.search(
            r"\blicen[cs]e\b|\bspdx\b|\bcc[-_ ]by\b|\bmit\b|\bapache\b|\bgpl\b",
            " ".join(match),
            flags=re.IGNORECASE,
        )
        for match in badge_matches
    )
    has_text_claim = bool(claimed_ids) and bool(
        re.search(
            r"\b(?:licensed|released|distributed|provided|available)\s+under\b|"
            r"\blicen[cs]e\s*:\s*",
            content,
            flags=re.IGNORECASE,
        )
    )
    has_claim = has_section or has_badge or has_text_claim
    if not has_claim:
        claimed_ids = []
    issues: List[str] = []

    if has_claim and not authority["claim_allowed"]:
        issues.append(
            "License claim is not authorized by repository evidence "
            f"(state: {authority['state']})"
        )

    root_evidence = authority["root_evidence"]
    authorized = authority["authorized_license"]
    if has_claim and authorized and claimed_ids:
        if any(claimed_id.lower() != authorized.lower() for claimed_id in claimed_ids):
            issues.append(
                "README license claim does not match the explicitly authorized "
                f"license ({authorized})"
            )

    if has_claim and len(root_evidence) == 1 and not authorized:
        evidence_path = root_evidence[0]
        linked_paths = {url.split("#", 1)[0] for _, url in extract_links(content)}
        if evidence_path not in linked_paths and f"./{evidence_path}" not in linked_paths:
            issues.append(f"License claim must link the evidence file: {evidence_path}")

        detected_id = authority["known_license_ids"].get(evidence_path)
        if claimed_ids and any(claimed_id != detected_id for claimed_id in claimed_ids):
            issues.append(
                "README license claim does not match the detected repository "
                f"license ({detected_id or 'unresolved custom terms'})"
            )

    return {
        **authority,
        "has_license_section": has_section,
        "has_license_badge": has_badge,
        "has_license_text_claim": has_text_claim,
        "claimed_license_ids": claimed_ids,
        "issues": issues,
        "valid": not issues,
    }


def count_unlabeled_fenced_code_blocks(content: str) -> int:
    """Count opening Markdown fences whose info string is empty.

    Fence meaning is stateful: a bare fence closes an existing block, but opens
    an unlabeled block when no block is active. Treating each fence as an
    independent regex match therefore misclassifies every valid closing fence.
    """
    fence_pattern = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})([^\r\n]*)$")
    open_fence_character = None
    open_fence_length = 0
    unlabeled_openings = 0

    for line in content.splitlines():
        match = fence_pattern.match(line)
        if not match:
            continue

        marker, info_string = match.groups()
        marker_character = marker[0]

        if open_fence_character is not None:
            is_closing_fence = (
                marker_character == open_fence_character
                and len(marker) >= open_fence_length
                and not info_string.strip()
            )
            if is_closing_fence:
                open_fence_character = None
                open_fence_length = 0
            continue

        # Backticks in a backtick fence's info string make it invalid Markdown,
        # so do not let that line alter parser state.
        if marker_character == "`" and "`" in info_string:
            continue

        if not info_string.strip():
            unlabeled_openings += 1

        open_fence_character = marker_character
        open_fence_length = len(marker)

    return unlabeled_openings


def check_markdown_formatting(content: str) -> List[str]:
    """Check for common markdown formatting issues."""
    issues = []

    lines = content.split('\n')

    # Check for lists without preceding blank line
    for i, line in enumerate(lines[1:], start=1):
        if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
            if i > 0 and lines[i-1].strip() and not re.match(r'^#+\s+', lines[i-1]):
                # Previous line is not blank and not a header
                if not (re.match(r'^\s*[-*+]\s+', lines[i-1]) or re.match(r'^\s*\d+\.\s+', lines[i-1])):
                    issues.append(f"Line {i+1}: List item should have blank line before it")

    # Check for code blocks without language specification
    unnamed_blocks = count_unlabeled_fenced_code_blocks(content)
    if unnamed_blocks > 0:
        issues.append(f"Found {unnamed_blocks} code block(s) without language specification")

    # Check for very long lines (> 120 chars, excluding URLs)
    for i, line in enumerate(lines, start=1):
        if len(line) > 120 and 'http' not in line:
            issues.append(f"Line {i}: Very long line ({len(line)} chars) - consider breaking")

    return issues

def check_header_structure(content: str) -> List[str]:
    """Check header structure and hierarchy."""
    issues = []
    lines = content.split('\n')

    h1_count = 0
    prev_level = 0

    for i, line in enumerate(lines, start=1):
        match = re.match(r'^(#+)\s+', line)
        if match:
            level = len(match.group(1))

            if level == 1:
                h1_count += 1

            # Check for skipped levels
            if prev_level > 0 and level > prev_level + 1:
                issues.append(f"Line {i}: Skipped header level (#{prev_level} to #{level})")

            prev_level = level

    if h1_count == 0:
        issues.append("No H1 header found (should have repository name)")
    elif h1_count > 1:
        issues.append(f"Multiple H1 headers found ({h1_count}) - should have only one")

    return issues

def validate_readme(
    file_path: str,
    repo_root: Optional[str] = None,
    authorized_license: Optional[str] = None,
) -> Dict:
    """Validate a README.md file and return detailed report."""
    path = Path(file_path)

    if not path.exists():
        return {
            'valid': False,
            'error': f"File not found: {file_path}",
            'score': 0
        }

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'valid': False,
            'error': f"Error reading file: {e}",
            'score': 0
        }

    repository_root = Path(repo_root).resolve() if repo_root else path.resolve().parent
    try:
        authority_report = check_license_authority(
            content,
            repository_root,
            authorized_license=authorized_license,
        )
    except ValueError as error:
        return {
            'valid': False,
            'error': str(error),
            'score': 0
        }

    report = {
        'valid': True,
        'file': str(path),
        'size': len(content),
        'sections': {},
        'links': {},
        'badges': {},
        'formatting': {},
        'headers': {},
        'license_authority': authority_report,
        'recommendations': [],
        'score': 0
    }

    # Check sections
    found_req, missing_req, found_rec, missing_rec = check_required_sections(content)
    report['sections'] = {
        'required_found': found_req,
        'required_missing': missing_req,
        'recommended_found': found_rec,
        'recommended_missing': missing_rec
    }

    # Extract and validate links
    links = extract_links(content)
    invalid_links = [url for text, url in links if not validate_url_format(url)]
    report['links'] = {
        'total': len(links),
        'invalid': invalid_links,
        'invalid_count': len(invalid_links)
    }

    # Extract badges
    badges = extract_badges(content)
    report['badges'] = {
        'count': len(badges),
        'urls': badges
    }

    # Check markdown formatting
    formatting_issues = check_markdown_formatting(content)
    report['formatting'] = {
        'issues': formatting_issues,
        'issue_count': len(formatting_issues)
    }

    # Check header structure
    header_issues = check_header_structure(content)
    report['headers'] = {
        'issues': header_issues,
        'issue_count': len(header_issues)
    }

    # Generate recommendations
    if missing_req:
        report['recommendations'].append(f"Add missing required sections: {', '.join(missing_req)}")

    if missing_rec:
        report['recommendations'].append(f"Consider adding recommended sections: {', '.join(missing_rec)}")

    if invalid_links:
        report['recommendations'].append(f"Fix {len(invalid_links)} invalid link(s)")

    if len(badges) == 0:
        report['recommendations'].append("Add badges for technologies used")

    if formatting_issues:
        report['recommendations'].append(f"Fix {len(formatting_issues)} formatting issue(s)")

    if header_issues:
        report['recommendations'].append(f"Fix {len(header_issues)} header structure issue(s)")

    if authority_report['issues']:
        report['valid'] = False
        report['recommendations'].extend(authority_report['issues'])

    # Calculate score (0-100)
    score = 100

    # Deduct for missing required sections (10 points each)
    score -= len(missing_req) * 10

    # Deduct for missing recommended sections (5 points each, max 20)
    score -= min(len(missing_rec) * 5, 20)

    # Deduct for invalid links (5 points each, max 15)
    score -= min(len(invalid_links) * 5, 15)

    # Deduct for no badges (10 points)
    if len(badges) == 0:
        score -= 10

    # Deduct for formatting issues (2 points each, max 15)
    score -= min(len(formatting_issues) * 2, 15)

    # Deduct for header issues (3 points each, max 10)
    score -= min(len(header_issues) * 3, 10)

    # Authority violations are a hard failure as well as a visible score cost.
    if authority_report['issues']:
        score -= 40

    report['score'] = max(0, score)

    return report

def format_report(report: Dict) -> str:
    """Format validation report as readable text."""
    if 'error' in report:
        return f"ERROR: {report.get('error', 'Unknown error')}"

    output = []
    output.append("=" * 60)
    output.append("README VALIDATION REPORT")
    output.append("=" * 60)
    output.append(f"\nFile: {report['file']}")
    output.append(f"Size: {report['size']:,} bytes")
    output.append(f"\nOVERALL SCORE: {report['score']}/100")

    # Score interpretation
    if report['score'] >= 90:
        output.append("Status: EXCELLENT ✓")
    elif report['score'] >= 75:
        output.append("Status: GOOD ✓")
    elif report['score'] >= 60:
        output.append("Status: ADEQUATE")
    else:
        output.append("Status: NEEDS IMPROVEMENT")

    # Sections
    output.append("\n" + "-" * 60)
    output.append("SECTIONS")
    output.append("-" * 60)

    sections = report['sections']
    output.append(f"Required sections: {len(sections['required_found'])}/{len(sections['required_found']) + len(sections['required_missing'])}")
    if sections['required_missing']:
        output.append(f"  Missing: {', '.join(sections['required_missing'])}")

    output.append(f"Recommended sections: {len(sections['recommended_found'])}/{len(sections['recommended_found']) + len(sections['recommended_missing'])}")
    if sections['recommended_missing']:
        output.append(f"  Missing: {', '.join(sections['recommended_missing'])}")

    # Links
    output.append("\n" + "-" * 60)
    output.append("LINKS")
    output.append("-" * 60)
    output.append(f"Total links: {report['links']['total']}")
    output.append(f"Invalid links: {report['links']['invalid_count']}")
    if report['links']['invalid']:
        for link in report['links']['invalid'][:5]:  # Show first 5
            output.append(f"  - {link}")
        if len(report['links']['invalid']) > 5:
            output.append(f"  ... and {len(report['links']['invalid']) - 5} more")

    # Badges
    output.append("\n" + "-" * 60)
    output.append("BADGES")
    output.append("-" * 60)
    output.append(f"Badge count: {report['badges']['count']}")

    # Formatting
    output.append("\n" + "-" * 60)
    output.append("FORMATTING")
    output.append("-" * 60)
    output.append(f"Issues found: {report['formatting']['issue_count']}")
    if report['formatting']['issues']:
        for issue in report['formatting']['issues'][:5]:  # Show first 5
            output.append(f"  - {issue}")
        if len(report['formatting']['issues']) > 5:
            output.append(f"  ... and {len(report['formatting']['issues']) - 5} more")

    # Headers
    output.append("\n" + "-" * 60)
    output.append("HEADER STRUCTURE")
    output.append("-" * 60)
    output.append(f"Issues found: {report['headers']['issue_count']}")
    if report['headers']['issues']:
        for issue in report['headers']['issues']:
            output.append(f"  - {issue}")

    authority = report['license_authority']
    output.append("\n" + "-" * 60)
    output.append("LICENSE AUTHORITY")
    output.append("-" * 60)
    output.append(f"Evidence state: {authority['state']}")
    output.append(
        "Root evidence: "
        + (", ".join(authority['root_evidence']) or "none")
    )
    output.append(
        "Scoped evidence: "
        + (", ".join(authority['scoped_evidence']) or "none")
    )
    output.append(f"Issues found: {len(authority['issues'])}")
    for issue in authority['issues']:
        output.append(f"  - {issue}")

    # Recommendations
    if report['recommendations']:
        output.append("\n" + "-" * 60)
        output.append("RECOMMENDATIONS")
        output.append("-" * 60)
        for i, rec in enumerate(report['recommendations'], start=1):
            output.append(f"{i}. {rec}")

    output.append("\n" + "=" * 60)

    return "\n".join(output)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Validate README presentation and claims.")
    parser.add_argument("readme")
    parser.add_argument("--repo-root")
    parser.add_argument("--authorized-license")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = validate_readme(
        args.readme,
        repo_root=args.repo_root,
        authorized_license=args.authorized_license,
    )
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(format_report(report))

    # Exit with error code if score is below 60
    if not report.get('valid', False) or report['score'] < 60:
        sys.exit(1)

if __name__ == '__main__':
    main()
