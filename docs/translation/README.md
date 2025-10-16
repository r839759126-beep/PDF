# Dilithium Translation Workflow

This directory contains the automated pipeline for extracting text from the Dilithium PDF, segmenting it by sections, and generating a Word document with Chinese translation.

## Overview

The workflow consists of three main scripts:

1. **extract_pdf.py** - Extracts text from PDF with section detection
2. **segment_sections.py** - Splits extracted text into section files
3. **export_docx.py** - Generates Word document with Chinese translation

## Prerequisites

- Python 3.10 or later
- pip (Python package manager)

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Local Workflow

### Step 1: Extract Text from PDF

Extract text from the Dilithium PDF file:

```bash
python scripts/extract_pdf.py Dilithium-uncompressed.pdf
```

This will create:
- `docs/out/Dilithium_en.md` - Structured Markdown with sections
- `docs/out/Dilithium_en.json` - JSON format with page and section data

**Options:**
```bash
python scripts/extract_pdf.py <pdf_file> [output_dir]
```

### Step 2: Segment Sections

Split the extracted content into individual section files:

```bash
python scripts/segment_sections.py docs/out/Dilithium_en.md
```

This will create section files in `docs/out/sections/`:
- `01_Abstract.md`
- `02_Introduction.md`
- `03_Related_Work.md`
- ... and so on

**Options:**
```bash
python scripts/segment_sections.py <input_file> [output_dir]
```

You can also use the JSON file as input:
```bash
python scripts/segment_sections.py docs/out/Dilithium_en.json docs/out/sections
```

### Step 3: Generate Word Document

Create the Word document with Chinese translation:

```bash
python scripts/export_docx.py
```

This will create `docs/out/Dilithium_zh.docx` with:
- Section headings
- Chinese translation (using human translations if available, otherwise placeholder)
- English reference text
- Applied terminology from glossary

**Options:**
```bash
python scripts/export_docx.py [sections_dir] [output_file] [glossary_file] [translation_dir]
```

### Complete Pipeline

Run all steps in sequence:

```bash
# Extract, segment, and export
python scripts/extract_pdf.py Dilithium-uncompressed.pdf && \
python scripts/segment_sections.py docs/out/Dilithium_en.md && \
python scripts/export_docx.py
```

## Directory Structure

```
.
├── scripts/
│   ├── extract_pdf.py         # PDF text extraction
│   ├── segment_sections.py    # Section segmentation
│   └── export_docx.py         # Word document generation
├── config/
│   └── terms_zh.yaml          # Terminology glossary (EN → ZH)
├── docs/
│   ├── out/                   # Generated outputs (gitignored)
│   │   ├── .gitkeep
│   │   ├── Dilithium_en.md
│   │   ├── Dilithium_en.json
│   │   ├── Dilithium_zh.docx
│   │   └── sections/
│   │       ├── 01_Abstract.md
│   │       ├── 02_Introduction.md
│   │       └── ...
│   └── translation/           # Human translations
│       ├── README.md
│       ├── STYLE_GUIDE.md
│       ├── GLOSSARY.md
│       └── sections/          # Section translations
│           ├── 01_Abstract.zh.md
│           ├── 02_Introduction.zh.md
│           └── ...
├── requirements.txt
└── .github/
    └── workflows/
        └── build-docs.yml     # CI/CD workflow
```

## Human Translation

To provide human translations:

1. Create or edit files in `docs/translation/sections/` with the `.zh.md` extension
2. Use the same base name as the English section file
3. Example: `01_Abstract.md` → `01_Abstract.zh.md`

The `export_docx.py` script will automatically use human translations when available.

### Translation File Format

```markdown
# Section Title

Chinese translation text goes here...

Multiple paragraphs are supported.
```

The first line (heading) is optional and will be removed if present.

## Terminology Glossary

The glossary is maintained in `config/terms_zh.yaml` with English → Chinese term mappings. These terms are:

1. Applied to placeholder translations automatically
2. Used for consistency across all sections
3. Documented in `docs/translation/GLOSSARY.md` for human translators

To add or modify terms:

1. Edit `config/terms_zh.yaml`
2. Update `docs/translation/GLOSSARY.md` accordingly
3. Re-run the export pipeline

## Style Guide

See `docs/translation/STYLE_GUIDE.md` for:
- Chinese translation conventions
- Punctuation rules
- Formatting guidelines
- When to keep English terms

## CI/CD Workflow

The GitHub Actions workflow automatically:

1. Runs on every push to `main` branch and on pull requests
2. Executes the complete extraction → segmentation → export pipeline
3. Uploads artifacts:
   - Dilithium_en.md
   - Dilithium_en.json
   - Section files (*.md)
   - Dilithium_zh.docx

Download artifacts from the "Actions" tab on GitHub after each workflow run.

## Troubleshooting

### PDF extraction fails

If PyMuPDF fails, the script will automatically fall back to pdfminer.six. If both fail, check:
- PDF file is not corrupted
- PDF file is readable (not password-protected)
- Sufficient memory is available

### Missing sections in output

The section detection uses heuristics and may miss some headings. You can:
- Manually edit `docs/out/sections/` files
- Adjust section patterns in `extract_pdf.py` (SECTION_PATTERNS)

### Glossary terms not applied

Check:
- `config/terms_zh.yaml` syntax is valid YAML
- Terms use exact case-insensitive matching
- Multi-word terms are properly quoted in YAML

### Word document formatting issues

The document uses python-docx library. For advanced formatting:
- Edit `scripts/export_docx.py`
- Modify styles, fonts, and layout as needed

## License

See repository LICENSE file.
