import sys
import subprocess
import os

# the scripts are used to extract requirements from pdfs using certain steps

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main_req_parser.py start_page end_page")
        sys.exit(1)

    # Get the start and end page numbers from the command-line arguments
    start_page = int(sys.argv[1])
    end_page = int(sys.argv[2])

    output_csv_file = 'output.csv'

    # Check if the output CSV file exists
    if os.path.exists(output_csv_file):
        # If it exists, delete it
        os.remove(output_csv_file)

    # Iterate through each page within the specified range
    for page_num in range(start_page, end_page + 1):

        # write pages from pdf to txt
        # write_pdf_pages_to_txt.py start_page end_page

        # Call write_pdf_pages_to_txt.py to write the current page to a text file
        subprocess.run(["python", "write_pdf_pages_to_txt.py", str(page_num), str(page_num)])

        # extract parse from txt to csv
        # req_parser_from_txt_to_csv.py

        # Call req_parser_from_txt_to_csv.py to extract and parse requirements from the text file
        subprocess.run(["python", "req_parser_from_txt_to_csv.py"])

    print("Extraction and parsing completed.")

if __name__ == "__main__":
    main()


