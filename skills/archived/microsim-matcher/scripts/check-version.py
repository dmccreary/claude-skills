#!/usr/bin/env python3
"""
Version Check Script for microsim-matcher Reference Files

This script checks if the local matching-criteria.md file is up-to-date
with the version on GitHub. It compares timestamps and warns if the
GitHub version is newer.

Usage:
    python check-version.py
    python check-version.py --quiet  # Exit code only, no output
    python check-version.py --update # Auto-update if outdated

Exit codes:
    0 - Local file is up-to-date
    1 - GitHub version is newer (outdated local file)
    2 - Error occurred (network, file not found, etc.)
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

# Configuration
GITHUB_REPO = "dmccreary/claude-skills"
FILE_PATH = "skills/microsim-matcher/references/matching-criteria.md"
LOCAL_FILE_PATH = Path(__file__).parent.parent / "references" / "matching-criteria.md"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/commits"


def get_local_file_timestamp():
    """Get the last modified timestamp of the local file."""
    try:
        if not LOCAL_FILE_PATH.exists():
            print(f"❌ Local file not found: {LOCAL_FILE_PATH}")
            return None

        timestamp = os.path.getmtime(LOCAL_FILE_PATH)
        return datetime.fromtimestamp(timestamp)
    except Exception as e:
        print(f"❌ Error reading local file timestamp: {e}")
        return None


def get_github_file_timestamp():
    """Get the last commit timestamp for the file on GitHub."""
    try:
        # GitHub API requires User-Agent header
        url = f"{GITHUB_API_URL}?path={FILE_PATH}&page=1&per_page=1"
        req = Request(url, headers={"User-Agent": "microsim-matcher-version-check"})

        with urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())

            if not data or len(data) == 0:
                print("❌ No commit history found on GitHub")
                return None

            # Get the date from the most recent commit
            commit_date_str = data[0]["commit"]["committer"]["date"]
            # Format: 2025-11-17T12:34:56Z
            commit_date = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")
            return commit_date

    except URLError as e:
        print(f"❌ Network error: {e}")
        print("   Make sure you have internet connection.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing GitHub API response: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def format_datetime(dt):
    """Format datetime for display."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def check_version(quiet=False):
    """
    Check if local file is up-to-date with GitHub version.

    Returns:
        0 if up-to-date
        1 if outdated
        2 if error
    """
    if not quiet:
        print("🔍 Checking microsim-matcher reference file version...")
        print()

    # Get local timestamp
    local_date = get_local_file_timestamp()
    if local_date is None:
        return 2

    if not quiet:
        print(f"📁 Local file:  {format_datetime(local_date)}")

    # Get GitHub timestamp
    github_date = get_github_file_timestamp()
    if github_date is None:
        if not quiet:
            print()
            print("⚠️  Could not check GitHub version (network error or API issue)")
            print("   Proceeding with local file...")
        return 2

    if not quiet:
        print(f"🌐 GitHub file: {format_datetime(github_date)}")
        print()

    # Compare timestamps
    if github_date > local_date:
        if not quiet:
            print("⚠️  WARNING: Reference File is Outdated")
            print()
            print(f"   Your local file was last modified on {format_datetime(local_date)}")
            print(f"   The GitHub version was updated on {format_datetime(github_date)}")
            print()
            print("   This may result in:")
            print("   • Missing information about new MicroSim generators")
            print("   • Outdated scoring guidelines")
            print("   • Incorrect recommendations")
            print()
            print("   Recommended actions:")
            print("   1. Update your local copy:")
            print("      git pull origin main")
            print()
            print("   2. Or download the latest version manually:")
            print(f"      https://github.com/{GITHUB_REPO}/blob/main/{FILE_PATH}")
            print()
        return 1
    else:
        if not quiet:
            print("✅ Local file is up-to-date!")
        return 0


def update_file():
    """Download and update the local file from GitHub."""
    print("📥 Downloading latest version from GitHub...")

    try:
        raw_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{FILE_PATH}"
        req = Request(raw_url, headers={"User-Agent": "microsim-matcher-version-check"})

        with urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')

        # Backup existing file
        if LOCAL_FILE_PATH.exists():
            backup_path = LOCAL_FILE_PATH.with_suffix('.md.backup')
            print(f"💾 Creating backup: {backup_path}")
            LOCAL_FILE_PATH.rename(backup_path)

        # Write new content
        LOCAL_FILE_PATH.write_text(content)
        print(f"✅ Successfully updated: {LOCAL_FILE_PATH}")
        return 0

    except Exception as e:
        print(f"❌ Error updating file: {e}")
        return 2


def main():
    parser = argparse.ArgumentParser(
        description="Check if microsim-matcher reference file is up-to-date"
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Quiet mode - exit code only, no output"
    )
    parser.add_argument(
        "--update", "-u",
        action="store_true",
        help="Automatically update if outdated"
    )

    args = parser.parse_args()

    # Check version
    result = check_version(quiet=args.quiet)

    # If outdated and update flag is set, update the file
    if result == 1 and args.update:
        if not args.quiet:
            print("🔄 Auto-update enabled, downloading latest version...")
            print()
        result = update_file()

    sys.exit(result)


if __name__ == "__main__":
    main()
