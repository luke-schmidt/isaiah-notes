#!/usr/bin/env python3
"""
Script to combine all chapter PDFs into main.pdf
"""

import os
import glob
import subprocess
import sys
from pathlib import Path

def find_chapter_pdfs():
    """Find all PDF files in chapter directories (excluding output folder)"""
    chapter_pdfs = []
    chapters_dir = Path("chapters")
    
    if not chapters_dir.exists():
        print("Error: chapters directory not found")
        return []
    
    # Look for PDF files in each chapter subdirectory
    for chapter_dir in sorted(chapters_dir.iterdir()):
        if chapter_dir.is_dir() and chapter_dir.name != "output":
            # Find PDF files in this chapter directory
            pdf_files = list(chapter_dir.glob("*.pdf"))
            if pdf_files:
                # Sort and take the first PDF (in case there are multiple)
                pdf_files.sort()
                chapter_pdfs.append(pdf_files[0])
                print(f"Found: {pdf_files[0]}")
    
    return chapter_pdfs

def combine_pdfs(pdf_files, output_file="main.pdf"):
    """Combine PDF files using ghostscript"""
    if not pdf_files:
        print("No PDF files found to combine")
        return False
    
    print(f"\nCombining {len(pdf_files)} PDFs into {output_file}...")
    
    # Use ghostscript to combine PDFs
    cmd = [
        "gs",
        "-dNOPAUSE",
        "-dBATCH",
        "-sDEVICE=pdfwrite",
        f"-sOutputFile={output_file}",
        "-dPDFSETTINGS=/prepress"
    ] + [str(pdf) for pdf in pdf_files]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully created {output_file}")
            return True
        else:
            print(f"Error combining PDFs: {result.stderr}")
            return False
    except FileNotFoundError:
        print("Error: ghostscript (gs) not found. Please install it with: brew install ghostscript")
        return False

def main():
    """Main function"""
    print("=== PDF Combiner ===")
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Find chapter PDFs
    chapter_pdfs = find_chapter_pdfs()
    
    if not chapter_pdfs:
        print("No chapter PDFs found")
        sys.exit(1)
    
    # Combine PDFs
    success = combine_pdfs(chapter_pdfs)
    
    if success:
        print("PDF combination completed successfully!")
    else:
        print("PDF combination failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
