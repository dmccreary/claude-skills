#!/usr/bin/env python3
"""
Extract structured text from a .docx file.

Outputs each paragraph with a style marker so the content can be converted
to structured JSX. Works without pandoc — uses only Python standard library.

Usage:
    python extract_docx.py document.docx [--output content.txt]

Output format:
    [Heading1] Section Title
    [Heading2] Subsection Title
    [Heading3] Sub-subsection Title
      - List item text
    Regular paragraph text
"""

import argparse
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def extract(docx_path: str) -> list[str]:
    """Extract paragraphs with style markers from a .docx file."""
    with zipfile.ZipFile(docx_path, "r") as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)

    root = tree.getroot()
    body = root.find(".//w:body", NS)
    if body is None:
        print("Error: No body element found in document.xml", file=sys.stderr)
        sys.exit(1)

    output = []
    for para in body.findall(".//w:p", NS):
        # Get paragraph style
        ppr = para.find("w:pPr", NS)
        style = ""
        if ppr is not None:
            pstyle = ppr.find("w:pStyle", NS)
            if pstyle is not None:
                style = pstyle.get(
                    "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val",
                    "",
                )

        # Get text content
        texts = []
        for r in para.findall(".//w:r", NS):
            for t in r.findall("w:t", NS):
                if t.text:
                    texts.append(t.text)

        text = "".join(texts).strip()
        if not text:
            continue

        if "Heading" in style or "Title" in style:
            output.append(f"[{style}] {text}")
        elif "ListParagraph" in style or "List" in style:
            output.append(f"  - {text}")
        else:
            output.append(text)

    return output


def main():
    parser = argparse.ArgumentParser(
        description="Extract structured text from a .docx file"
    )
    parser.add_argument("docx", help="Path to the .docx file")
    parser.add_argument(
        "--output", "-o", help="Output file path (default: stdout)", default=None
    )
    args = parser.parse_args()

    if not Path(args.docx).exists():
        print(f"Error: File not found: {args.docx}", file=sys.stderr)
        sys.exit(1)

    lines = extract(args.docx)
    content = "\n".join(lines)

    if args.output:
        Path(args.output).write_text(content, encoding="utf-8")
        print(f"Extracted {len(lines)} paragraphs to {args.output}", file=sys.stderr)
    else:
        print(content)


if __name__ == "__main__":
    main()
