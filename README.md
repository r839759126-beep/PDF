# Dilithium PDF Translation Pipeline

Automated pipeline for extracting text from the Dilithium cryptographic paper PDF, segmenting it by sections, and generating a Word document with Chinese translation.

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running the Pipeline

Extract, segment, and export in one command:

```bash
python scripts/extract_pdf.py Dilithium-uncompressed.pdf && \
python scripts/segment_sections.py docs/out/Dilithium_en.md && \
python scripts/export_docx.py
```

Or run steps individually:

```bash
# 1. Extract text from PDF
python scripts/extract_pdf.py Dilithium-uncompressed.pdf

# 2. Segment into section files
python scripts/segment_sections.py docs/out/Dilithium_en.md

# 3. Generate Word document
python scripts/export_docx.py
```

### Verify Pipeline

```bash
python scripts/verify_pipeline.py
```

## Output Files

The pipeline generates:

- `docs/out/Dilithium_en.md` - Extracted text in Markdown format
- `docs/out/Dilithium_en.json` - Extracted text with page and section metadata
- `docs/out/sections/*.md` - Individual section files
- `docs/out/Dilithium_zh.docx` - Word document with Chinese translation

## Documentation

See [docs/translation/README.md](docs/translation/README.md) for detailed workflow documentation.

Key resources:
- **Workflow Guide**: [docs/translation/README.md](docs/translation/README.md)
- **Style Guide**: [docs/translation/STYLE_GUIDE.md](docs/translation/STYLE_GUIDE.md)
- **Glossary**: [docs/translation/GLOSSARY.md](docs/translation/GLOSSARY.md)
- **Terminology Config**: [config/terms_zh.yaml](config/terms_zh.yaml)

## CI/CD

The GitHub Actions workflow ([.github/workflows/build-docs.yml](.github/workflows/build-docs.yml)) automatically runs the complete pipeline on every push and pull request. Download artifacts from the Actions tab.

## Adding Human Translations

1. Create translation files in `docs/translation/sections/` with `.zh.md` extension
2. Use the same base name as the English section file (e.g., `01_Abstract.zh.md`)
3. The export script will automatically use human translations when available

Example:

```bash
# Create a translation file
cat > docs/translation/sections/03_Introduction.zh.md << 'EOF'
# Introduction

在这里填写中文翻译...
EOF

# Regenerate Word document
python scripts/export_docx.py
```

## Project Structure

```
.
├── scripts/                    # Python scripts
│   ├── extract_pdf.py          # PDF text extraction
│   ├── segment_sections.py     # Section segmentation
│   ├── export_docx.py          # Word document generation
│   └── verify_pipeline.py      # Pipeline verification
├── config/
│   └── terms_zh.yaml           # Terminology glossary (EN → ZH)
├── docs/
│   ├── out/                    # Generated outputs (gitignored)
│   │   ├── Dilithium_en.md
│   │   ├── Dilithium_en.json
│   │   ├── Dilithium_zh.docx
│   │   └── sections/
│   └── translation/            # Documentation and human translations
│       ├── README.md
│       ├── STYLE_GUIDE.md
│       ├── GLOSSARY.md
│       └── sections/           # Human translation files
├── requirements.txt
└── .github/
    └── workflows/
        └── build-docs.yml      # CI/CD workflow
```

## Features

- **Multi-backend PDF extraction**: Uses PyMuPDF with automatic fallback to pdfminer.six
- **Automatic section detection**: Regex-based heading detection for paper sections
- **Terminology consistency**: YAML-based glossary for standardized translations
- **Human translation support**: Override placeholders with human translations
- **Cross-platform**: Works on Linux, macOS, and Windows
- **CI/CD ready**: Automated builds via GitHub Actions

## Contributing

To add or update terminology:

1. Edit `config/terms_zh.yaml`
2. Update `docs/translation/GLOSSARY.md` accordingly
3. Re-run the pipeline to apply changes

To improve extraction or formatting:

1. Edit the respective script in `scripts/`
2. Test locally
3. Verify with `python scripts/verify_pipeline.py`

## License

See repository LICENSE file.

## Notes

- The generated Word document (`.docx`) is not committed to the repository to avoid bloating
- Download artifacts from GitHub Actions to access the latest generated files
- The original PDF files are preserved and not modified by the pipeline
