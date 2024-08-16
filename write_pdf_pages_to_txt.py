import sys
import PyPDF2
import os
import re


# Function to determine if a line should be skipped
def should_skip_line(line):
    # Regex pattern to match chapter, subchapter, and sub-subchapter lines
    pattern = r'^\d+(\.\d+)+\s+.*$'
    return not line.strip() or re.match(pattern, line.strip()) or line.startswith('[BsM')


# Get the start page and end page numbers from the command-line arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <start_page> <end_page>")
    sys.exit(1)

try:
    start_page = int(sys.argv[1])
    end_page = int(sys.argv[2])
except ValueError:
    print("Invalid page numbers. Please provide valid integers.")
    sys.exit(1)

# Get a list of files in the current directory
files = os.listdir()

# Find the first PDF file in the list
pdf_file = next((file for file in files if file.lower().endswith('.pdf')), None)

# Check if a PDF file was found
if pdf_file:
    # Open the PDF file for reading
    with open(pdf_file, 'rb') as pdf_file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize a variable to store the extracted text
        extracted_text = ""

        # Iterate through the specified range of pages
        for page_num in range(start_page - 1, end_page):
            # Get the content of the current page
            page_content = pdf_reader.pages[page_num].extract_text()

            # Split the page content into lines
            lines = page_content.split('\n')

            # Filter out unwanted lines
            filtered_lines = [line for line in lines if not should_skip_line(line)]

            # Concatenate the filtered lines
            filtered_page_content = '\n'.join(filtered_lines)

            # Append the filtered page content to the extracted text
            extracted_text += filtered_page_content

    # Write the extracted text to a text file
    with open('output.txt', 'w', encoding='utf-8') as output_txt_file:
        output_txt_file.write(extracted_text)

    print(f"Pages {start_page} to {end_page} content has been written to output.txt")
else:
    print("No PDF files found in the current directory.")
