#!/usr/bin/env python3
"""
Extract text from PDF file with structured output.

This script extracts text from a PDF file page-by-page using PyMuPDF (fitz)
with fallback to pdfminer.six. It normalizes whitespace, fixes common 
hyphenation at line breaks, and attempts light heading detection for sections.

Output:
- docs/out/Dilithium_en.md: Structured Markdown with headings and paragraphs
- docs/out/Dilithium_en.json: Structured JSON with pages and detected sections
"""

import sys
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple, Optional

try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False
    print("Warning: PyMuPDF not available, will use pdfminer.six as fallback")

try:
    from pdfminer.high_level import extract_text as pdfminer_extract
    PDFMINER_AVAILABLE = True
except ImportError:
    PDFMINER_AVAILABLE = False
    print("Warning: pdfminer.six not available")


# Common section headings to detect
SECTION_PATTERNS = [
    r'^Abstract\s*$',
    r'^\d+\.?\s+Introduction\s*$',
    r'^\d+\.?\s+Related\s+Work\s*$',
    r'^\d+\.?\s+Preliminaries\s*$',
    r'^\d+\.?\s+Construction\s*$',
    r'^\d+\.?\s+Security\s*$',
    r'^\d+\.?\s+Security\s+Analysis\s*$',
    r'^\d+\.?\s+Implementation\s*$',
    r'^\d+\.?\s+Performance\s*$',
    r'^\d+\.?\s+Evaluation\s*$',
    r'^\d+\.?\s+Conclusion\s*$',
    r'^\d+\.?\s+Conclusions\s*$',
    r'^References\s*$',
    r'^Bibliography\s*$',
    r'^Acknowledgments?\s*$',
    r'^Appendix\s*[A-Z]?\s*$',
]


def normalize_text(text: str) -> str:
    """Normalize whitespace and fix common issues in extracted text."""
    if not text:
        return ""
    
    # Fix hyphenation at line breaks (e.g., "crypto-\ngraphic" -> "cryptographic")
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    
    # Normalize multiple spaces to single space
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Normalize multiple newlines (keep at most 2)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    # Remove trailing spaces from lines
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    
    return text.strip()


def is_section_heading(line: str) -> bool:
    """Check if a line is likely a section heading."""
    line = line.strip()
    for pattern in SECTION_PATTERNS:
        if re.match(pattern, line, re.IGNORECASE):
            return True
    
    # Also check for lines that are short, all caps, or start with number
    if len(line) < 50 and (line.isupper() or re.match(r'^\d+\.?\s+[A-Z]', line)):
        return True
    
    return False


def extract_with_pymupdf(pdf_path: str) -> Tuple[str, List[Dict]]:
    """Extract text using PyMuPDF (fitz)."""
    doc = fitz.open(pdf_path)
    full_text = []
    pages_data = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        normalized = normalize_text(text)
        
        full_text.append(normalized)
        pages_data.append({
            "page": page_num + 1,
            "text": normalized
        })
    
    doc.close()
    return "\n\n".join(full_text), pages_data


def extract_with_pdfminer(pdf_path: str) -> Tuple[str, List[Dict]]:
    """Extract text using pdfminer.six as fallback."""
    text = pdfminer_extract(pdf_path)
    normalized = normalize_text(text)
    
    # pdfminer doesn't give us page-by-page info easily, so we return one page
    pages_data = [{
        "page": 1,
        "text": normalized
    }]
    
    return normalized, pages_data


def detect_sections(text: str) -> List[Dict[str, str]]:
    """Detect sections in the text based on heading patterns."""
    lines = text.split('\n')
    sections = []
    current_section = None
    current_content = []
    
    for line in lines:
        if is_section_heading(line):
            # Save previous section
            if current_section:
                sections.append({
                    "title": current_section,
                    "content": '\n'.join(current_content).strip()
                })
            
            # Start new section
            current_section = line.strip()
            current_content = []
        else:
            current_content.append(line)
    
    # Save last section
    if current_section:
        sections.append({
            "title": current_section,
            "content": '\n'.join(current_content).strip()
        })
    elif current_content:
        # No sections detected, save all as single section
        sections.append({
            "title": "Document",
            "content": '\n'.join(current_content).strip()
        })
    
    return sections


def generate_markdown(sections: List[Dict[str, str]]) -> str:
    """Generate Markdown format from sections."""
    md_lines = []
    
    for section in sections:
        title = section["title"]
        content = section["content"]
        
        # Determine heading level (# or ##)
        if re.match(r'^\d+\.', title):
            md_lines.append(f"# {title}\n")
        else:
            md_lines.append(f"# {title}\n")
        
        md_lines.append(content)
        md_lines.append("")  # Blank line between sections
    
    return '\n'.join(md_lines)


def extract_pdf(pdf_path: str, output_dir: str) -> None:
    """Main function to extract PDF and generate outputs."""
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting text from {pdf_path}...")
    
    # Try PyMuPDF first, fallback to pdfminer
    if PYMUPDF_AVAILABLE:
        try:
            full_text, pages_data = extract_with_pymupdf(str(pdf_path))
            print(f"✓ Extracted {len(pages_data)} pages using PyMuPDF")
        except Exception as e:
            print(f"PyMuPDF extraction failed: {e}")
            if PDFMINER_AVAILABLE:
                full_text, pages_data = extract_with_pdfminer(str(pdf_path))
                print(f"✓ Extracted text using pdfminer.six")
            else:
                raise RuntimeError("No PDF extraction library available")
    elif PDFMINER_AVAILABLE:
        full_text, pages_data = extract_with_pdfminer(str(pdf_path))
        print(f"✓ Extracted text using pdfminer.six")
    else:
        raise RuntimeError("No PDF extraction library available. Please install PyMuPDF or pdfminer.six")
    
    # Detect sections
    print("Detecting sections...")
    sections = detect_sections(full_text)
    print(f"✓ Detected {len(sections)} sections")
    
    # Generate Markdown
    print("Generating Markdown output...")
    markdown = generate_markdown(sections)
    md_output = output_dir / "Dilithium_en.md"
    md_output.write_text(markdown, encoding='utf-8')
    print(f"✓ Saved Markdown to {md_output}")
    
    # Generate JSON
    print("Generating JSON output...")
    json_data = {
        "source_file": pdf_path.name,
        "total_pages": len(pages_data),
        "pages": pages_data,
        "sections": sections
    }
    json_output = output_dir / "Dilithium_en.json"
    json_output.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"✓ Saved JSON to {json_output}")
    
    print("\nExtraction complete!")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <pdf_file> [output_dir]")
        print("Example: python extract_pdf.py Dilithium-uncompressed.pdf docs/out")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs/out"
    
    if not Path(pdf_file).exists():
        print(f"Error: PDF file not found: {pdf_file}")
        sys.exit(1)
    
    extract_pdf(pdf_file, output_dir)


if __name__ == "__main__":
    main()
