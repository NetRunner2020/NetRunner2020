import os
import re

def preprocess_text(text):
    """Perform basic text preprocessing."""
    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def preprocess_extracted_text(input_dir, output_dir):
    """Preprocess all extracted text files in input_dir and save to output_dir."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    for text_file in os.listdir(input_dir):
        if text_file.endswith('.txt'):
            text_path = os.path.join(input_dir, text_file)
            with open(text_path, 'r', encoding='utf-8') as f:
                text = f.read()

            # Preprocess the text
            preprocessed_text = preprocess_text(text)

            # Save the preprocessed text
            preprocessed_filename = text_file.replace('.txt', '_preprocessed.txt')
            preprocessed_path = os.path.join(output_dir, preprocessed_filename)
            with open(preprocessed_path, 'w', encoding='utf-8') as f:
                f.write(preprocessed_text)
            print(f"Preprocessed text saved to: {preprocessed_path}")

if __name__ == "__main__":
    input_dir = '../data/extracted_data/'  # Directory containing extracted text
    output_dir = '../data/preprocessed_data/'  # Directory to save preprocessed text
    preprocess_extracted_text(input_dir, output_dir)
    print("Text preprocessing complete.")
