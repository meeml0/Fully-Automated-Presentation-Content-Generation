
import os
import re
import argparse
import sys
from pypdf import PdfReader, PdfWriter

def sanitize_filename(name):
    """
    Cleans invalid characters for file names.
    """
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

def analyze_and_split_pdf(pdf_path, output_dir=None):
    """
    Analyzes the PDF structure (Bookmarks/Outline) and splits it into sections.
    """
    print(f"Loading PDF: {pdf_path}")
    if not os.path.exists(pdf_path):
        print(f"Error: File not found -> {pdf_path}")
        return

    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    total_pages = len(reader.pages)
    print(f"Total Pages: {total_pages}")
    
    # Analyze Structure (Outline)
    print("\n--- Analyzing PDF Structure ---")
    outline = reader.outline
    
    sections = []
    
    if outline:
        print("Table of Contents (Outline) found.")
        
        # Flatten the outline logic simply for main chapters
        # (This logic mimics the user's provided sample)
        for item in outline:
            if isinstance(item, list):
                # Skipping sub-sections as per original logic to focus on main chapters
                continue
            else:
                try:
                    title = item.title
                    # In pypdf, reader.get_destination_page_number(item) retrieves the page index
                    page_num = reader.get_destination_page_number(item)
                    sections.append((title, page_num))
                except Exception as e:
                    continue
    else:
        print("Warning: No internal outline found on this PDF.")
        print("Cannot split comfortably without context.")
        return

    if not sections:
        print("No valid sections extractable from outline.")
        return

    # Sort by page number to ensure order
    sections.sort(key=lambda x: x[1])
    
    # Filter out invalid page numbers
    sections = [s for s in sections if 0 <= s[1] < total_pages]

    print(f"\nFound {len(sections)} sections.")

    # Determine Output Directory
    if output_dir is None:
        base_folder = os.path.dirname(os.path.abspath(pdf_path))
        output_dir = os.path.join(base_folder, "Split_Sections")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Process and Save Sections
    for i in range(len(sections)):
        title, start_page = sections[i]
        
        # Determine end page
        if i + 1 < len(sections):
            end_page = sections[i+1][1]
        else:
            end_page = total_pages # Last section goes to the end of file
        
        # Check valid range
        if end_page <= start_page:
            continue

        safe_title = sanitize_filename(title)
        # Naming format: "Section Name.pdf"
        output_filename = os.path.join(output_dir, f"{safe_title}.pdf")
        
        print(f"[{i+1}/{len(sections)}] Saving: '{title}' (Pages {start_page+1}-{end_page})")
        
        writer = PdfWriter()
        # Copy pages
        for p_idx in range(start_page, end_page):
            writer.add_page(reader.pages[p_idx])
        
        # Write file
        try:
            with open(output_filename, "wb") as f_out:
                writer.write(f_out)
        except Exception as e:
            print(f"Failed to write section {safe_title}: {e}")
    
    print(f"\nProcessing Complete! Files saved in: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Split PDF book into sections based on Bookmarks/Outline.")
    parser.add_argument("input_pdf", help="Path to the source PDF file.")
    parser.add_argument("--output_dir", help="Custom output directory.", default=None)
    
    args = parser.parse_args()
    
    analyze_and_split_pdf(args.input_pdf, args.output_dir)

if __name__ == "__main__":
    main()
