import os
from tika import parser  # Apache Tika for PDF parsing

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF using Apache Tika."""
    try:
        parsed_pdf = parser.from_file(pdf_path)
        text = parsed_pdf.get('content', '')  # Get the content (text) from parsed data
        if not text:
            print(f"No text found in: {pdf_path}")
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def extract_text_from_pdfs(input_dir, output_dir):
    """Extract text from all PDFs in input_dir and save to output_dir."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, pdf_file)
            text = extract_text_from_pdf(pdf_path)  # Extract text

            if text:  # Save extracted text only if it's not empty
                text_filename = pdf_file.replace('.pdf', '.txt')
                text_path = os.path.join(output_dir, text_filename)
                with open(text_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Extracted text saved to: {text_path}")
            else:
                print(f"Skipped: No text found in {pdf_file}")

if __name__ == "__main__":
    input_dir = '../data/pdf_files/'  # Directory containing PDFs
    output_dir = '../data/extracted_data/'  # Directory to save extracted text
    extract_text_from_pdfs(input_dir, output_dir)
    print("PDF text extraction complete.")
