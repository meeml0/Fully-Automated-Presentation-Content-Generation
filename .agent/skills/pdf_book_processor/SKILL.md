---
name: pdf_book_processor
description: Intelligent PDF processing skill that analyzes book structure (Table of Contents/Bookmarks) and splits the PDF into separate files for each chapter or section.
---

# PDF Book Processor Skill

This skill allows you to process large PDF textbooks and split them into smaller, manageable files based on their internal Table of Contents (Outline/Bookmarks). It preserves the context and naming conventions found in the file.

## Features

1.  **Structure Analysis**: Reads the internal PDF outline (bookmarks) to understand the book's structure.
2.  **Intelligent Splitting**: Splits the PDF into separate files for each detected section/chapter.
3.  **Smart Naming**: Automatically names the output files using the section titles (sanitized for file system compatibility).
4.  **Context Aware**: Identifies the start and end pages of each section contextually.

## Usage

Use the `extract_sections.py` script to process a PDF file.

### Basic Command

```bash
python .agent/skills/pdf_book_processor/scripts/extract_sections.py "path/to/your/book.pdf"
```

### Arguments

-   `input_pdf` (Required): Path to the source PDF file.
-   `--output_dir` (Optional): Directory where split files will be saved. Default is `Split_Sections` inside the source folder.

## Example

To split a book named `Walpole.pdf` located in the current directory:

```bash
python .agent/skills/pdf_book_processor/scripts/extract_sections.py "Walpole.pdf"
```
