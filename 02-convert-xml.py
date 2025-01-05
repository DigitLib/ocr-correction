import os
from lxml import etree


def convert_to_txt(filepath, output_folder):
    # Load the TEI XML file
    parser = etree.XMLParser(encoding='utf-8')
    tree = etree.parse(filepath, parser)
    root = tree.getroot()

    # Handle namespaces if any
    namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}
    body_element = root.find('.//tei:body', namespaces)

    if body_element is not None:
        text_elements = body_element.findall('.//tei:p', namespaces)

        # Debugging: Print extracted elements to ensure they are correct
        print(f"Extracted Elements from {filepath}:")
        for element in text_elements:
            print(element.tag, element.text or '', "Attributes:", element.attrib)
            print(etree.tostring(element).decode('utf-8'))  # Print full XML of the element
        print("-" * 80)

        # Join texts with newline characters to separate paragraphs
        text_content = '\n'.join([element.text.strip() for element in text_elements if element.text is not None])

        # Debugging: Print extracted text to ensure it's not empty
        print(f"Extracted Text from {filepath}:")
        print(text_content or 'No text extracted')
        print("-" * 80)

        # Write the text to a new TXT file in the specified output folder
        txt_filename = os.path.splitext(os.path.basename(filepath))[0] + '.txt'
        txt_filepath = os.path.join(output_folder, txt_filename)
        with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
    else:
        print(f"No <body> element found in {filepath}.")

# Define the source and output folders
source_folder = '/path/to/corrected_xml'
output_folder = '/path/to/corrected_txt'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created output folder: {output_folder}")

# Iterate over all files in the "corrected" folder
for filename in os.listdir(source_folder):
    if filename.endswith('.xml'):
        filepath = os.path.join(source_folder, filename)
        convert_to_txt(filepath, output_folder)

print("Conversion completed successfully.")