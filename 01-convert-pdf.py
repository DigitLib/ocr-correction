import os
from PyPDF2 import PdfReader

# Define paths for input and output folders
input_folder = '/path/to/pdf_ocr'
output_folder = 'parh/to/export_raw_txt'

# Create 'raw_txt' folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def extract_text_from_pdf(pdf_path, txt_path):
    try:
        with open(pdf_path, 'rb') as fh:
            pdf = PdfReader(fh)
            text = ''
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text() or ''
            return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

# List all PDF files in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

for file in pdf_files:
    # Construct full paths for the PDF and TXT files
    pdf_path = os.path.join(input_folder, file)
    txt_filename = os.path.splitext(file)[0] + '.txt'
    txt_path = os.path.join(output_folder, txt_filename)

    # Extract text from the PDF and save it to a TXT file
    text = extract_text_from_pdf(pdf_path, txt_path)
    if text is not None:
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

print("Text extraction complete.")
