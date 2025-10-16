#!/usr/bin/env python3
"""
Segment extracted text into section-based Markdown files.

This script consumes Dilithium_en.md or Dilithium_en.json and splits
into section-based Markdown files under docs/out/sections/*.md
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict


def sanitize_filename(title: str) -> str:
    """Convert section title to a safe filename."""
    # Remove or replace unsafe characters
    title = re.sub(r'[^\w\s-]', '', title)
    title = re.sub(r'\s+', '_', title)
    return title.strip('_')


def read_from_json(json_path: Path) -> List[Dict[str, str]]:
    """Read sections from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('sections', [])


def read_from_markdown(md_path: Path) -> List[Dict[str, str]]:
    """Read sections from Markdown file."""
    content = md_path.read_text(encoding='utf-8')
    sections = []
    
    # Split by markdown headers (# Title)
    parts = re.split(r'\n# (.+)\n', content)
    
    # First part might be before any header
    if parts[0].strip():
        sections.append({
            "title": "Preface",
            "content": parts[0].strip()
        })
    
    # Process pairs of (title, content)
    for i in range(1, len(parts), 2):
        if i + 1 < len(parts):
            sections.append({
                "title": parts[i].strip(),
                "content": parts[i + 1].strip()
            })
        else:
            sections.append({
                "title": parts[i].strip(),
                "content": ""
            })
    
    return sections


def segment_sections(input_file: str, output_dir: str) -> None:
    """Main function to segment sections into separate files."""
    input_path = Path(input_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Reading sections from {input_path}...")
    
    # Determine input format and read sections
    if input_path.suffix == '.json':
        sections = read_from_json(input_path)
    elif input_path.suffix == '.md':
        sections = read_from_markdown(input_path)
    else:
        raise ValueError(f"Unsupported file format: {input_path.suffix}. Use .json or .md")
    
    print(f"✓ Found {len(sections)} sections")
    
    # Write each section to a separate file
    print(f"Writing section files to {output_dir}...")
    
    for idx, section in enumerate(sections, start=1):
        title = section["title"]
        content = section["content"]
        
        # Create filename: 01_Abstract.md, 02_Introduction.md, etc.
        safe_title = sanitize_filename(title)
        filename = f"{idx:02d}_{safe_title}.md"
        file_path = output_dir / filename
        
        # Write section as Markdown
        section_md = f"# {title}\n\n{content}\n"
        file_path.write_text(section_md, encoding='utf-8')
        
        print(f"  ✓ {filename}")
    
    print(f"\n✓ Segmented {len(sections)} sections into {output_dir}")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python segment_sections.py <input_file> [output_dir]")
        print("Example: python segment_sections.py docs/out/Dilithium_en.md docs/out/sections")
        print("         python segment_sections.py docs/out/Dilithium_en.json docs/out/sections")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs/out/sections"
    
    if not Path(input_file).exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    segment_sections(input_file, output_dir)


if __name__ == "__main__":
    main()
