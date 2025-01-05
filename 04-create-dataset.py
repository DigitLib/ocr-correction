import os
import pandas as pd
import json

# Define folder paths
corrected_txt_folder = '/path/corrected_txt_merged'
raw_txt_folder = '/path/to/raw_txt_merged'
output_file = 'combined_dataset.jsonl'  # JSONL output file

# Read the CSV file into a DataFrame
files_df = pd.read_csv('/path/to/files_list.csv', header=None)

# Print the first few rows of the DataFrame to ensure it's loaded correctly
print(files_df.head())

# Initialize an empty list to store combined data
combined_data = []

# Loop through each row in the DataFrame
for idx, row in files_df.iterrows():
    corrected_file_path = os.path.join(corrected_txt_folder, row[1])
    raw_ocr_file_path = os.path.join(raw_txt_folder, row[0])

    # Print file paths to verify they are correct
    print(f"Corrected File Path: {corrected_file_path}")
    print(f"Raw OCR File Path: {raw_ocr_file_path}")

    # Check if both files exist
    if not (os.path.exists(corrected_file_path) and os.path.exists(raw_ocr_file_path)):
        print(f"Files not found for {row[0]} and {row[1]}")
        continue

    # Read the contents of both files
    with open(corrected_file_path, 'r', encoding='utf-8') as corrected_file:
        corrected_content = corrected_file.read()

    with open(raw_ocr_file_path, 'r', encoding='utf-8') as raw_ocr_file:
        raw_ocr_content = raw_ocr_file.read()

    # Combine the contents (this is just an example; adjust based on your needs)
    combined_content = {
        'file_name': row[0],
        'corrected_text': corrected_content,
        'raw_ocr_text': raw_ocr_content
    }

    # Append to the combined data list
    combined_data.append(combined_content)

# Write the combined data to a JSONL file
with open(output_file, 'w', encoding='utf-8') as jsonl_file:
    for item in combined_data:
        jsonl_file.write(json.dumps(item, ensure_ascii=False) + '\n')
print("Combining complete. Check the output file for results.")