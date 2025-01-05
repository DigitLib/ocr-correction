import os
import glob

# Define source and destination directories (! change path for raw_txt when merge raw text)
source_dir = '/path/to/corrected_txt'
destination_dir = '/path/to/corrected_txt_merged'

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Get a list of all .xml.txt files in the source directory
file_paths = glob.glob(os.path.join(source_dir, '*.txt'))

for file_path in file_paths:
    # Extract the base name of the file (without extension)
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Define the output file path
    output_file_path = os.path.join(destination_dir, f'{base_name}_merged.txt')

    # Read the contents of the file and merge lines
    with open(file_path, 'r') as f:
        merged_content = " ".join(line.strip("\n") for line in f)

    # Write the merged content to the output file
    with open(output_file_path, 'w') as f:
        f.write(merged_content)

print("Merging complete.")
