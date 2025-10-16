#!/usr/bin/env python3
"""
Test script to verify the pipeline execution.
"""

import sys
from pathlib import Path

def test_pipeline():
    """Test that all pipeline outputs are generated."""
    errors = []
    
    # Check output files
    required_files = [
        "docs/out/Dilithium_en.md",
        "docs/out/Dilithium_en.json",
        "docs/out/Dilithium_zh.docx",
    ]
    
    for file_path in required_files:
        if not Path(file_path).exists():
            errors.append(f"Missing required file: {file_path}")
        else:
            size = Path(file_path).stat().st_size
            print(f"✓ {file_path} ({size} bytes)")
    
    # Check section files
    sections_dir = Path("docs/out/sections")
    if not sections_dir.exists():
        errors.append("Missing sections directory: docs/out/sections")
    else:
        section_files = list(sections_dir.glob("*.md"))
        if len(section_files) == 0:
            errors.append("No section files found in docs/out/sections")
        else:
            print(f"✓ docs/out/sections/ ({len(section_files)} section files)")
    
    # Check configuration files
    config_files = [
        "config/terms_zh.yaml",
        "requirements.txt",
        ".gitignore",
    ]
    
    for file_path in config_files:
        if not Path(file_path).exists():
            errors.append(f"Missing config file: {file_path}")
        else:
            print(f"✓ {file_path}")
    
    # Check documentation
    doc_files = [
        "docs/translation/README.md",
        "docs/translation/STYLE_GUIDE.md",
        "docs/translation/GLOSSARY.md",
    ]
    
    for file_path in doc_files:
        if not Path(file_path).exists():
            errors.append(f"Missing documentation: {file_path}")
        else:
            print(f"✓ {file_path}")
    
    # Check scripts
    script_files = [
        "scripts/extract_pdf.py",
        "scripts/segment_sections.py",
        "scripts/export_docx.py",
    ]
    
    for file_path in script_files:
        if not Path(file_path).exists():
            errors.append(f"Missing script: {file_path}")
        else:
            print(f"✓ {file_path}")
    
    # Check CI workflow
    if not Path(".github/workflows/build-docs.yml").exists():
        errors.append("Missing CI workflow: .github/workflows/build-docs.yml")
    else:
        print(f"✓ .github/workflows/build-docs.yml")
    
    # Report results
    print("\n" + "="*60)
    if errors:
        print("FAILED: Pipeline verification failed with errors:\n")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    else:
        print("SUCCESS: All pipeline files generated successfully!")
        print("\nNext steps:")
        print("  1. The CI workflow will run automatically on push")
        print("  2. Download artifacts from GitHub Actions")
        print("  3. Add human translations to docs/translation/sections/")
        return 0

if __name__ == "__main__":
    sys.exit(test_pipeline())
