# Load the required libraries
library(pdftools)
library(tesseract)

# Function to extract text from a single PDF
extract_text_from_pdf <- function(pdf_path) {
  tryCatch({
    # Extract text from the PDF using pdftools
    text <- pdf_text(pdf_path)
    
    if (length(text) == 0) {
      message("No text found in: ", pdf_path)
      return(NULL)
    }
    
    return(text)
  }, error = function(e) {
    message("Error extracting text from ", pdf_path, ": ", e$message)
    return(NULL)
  })
}

# Function to extract text from all PDFs in a directory and save the extracted text to files
extract_text_from_pdfs <- function(input_dir, output_dir) {
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)  # Create output directory if it doesn't exist
  }
  
  pdf_files <- list.files(input_dir, pattern = "\\.pdf$", full.names = TRUE)
  
  for (pdf_file in pdf_files) {
    text <- extract_text_from_pdf(pdf_file)  # Extract text
    
    if (!is.null(text)) {
      # Save the extracted text to a .txt file
      text_filename <- sub("\\.pdf$", ".txt", basename(pdf_file))
      text_path <- file.path(output_dir, text_filename)
      writeLines(text, text_path)
      message("Extracted text saved to: ", text_path)
    } else {
      message("Skipped: No text found in ", pdf_file)
    }
  }
}

# Main code
input_dir <- "C:/Users/Christopher/OneDrive/Documents/PDF"  # Directory containing PDFs
output_dir <- "C:/Users/Christopher/Documents/extracted_texts"  # Directory to save extracted text
extract_text_from_pdfs(input_dir, output_dir)

message("PDF text extraction complete.")
