## OCR Correction files for dataset creation
This repo contain python files that is used for creation of [this dataset](https://huggingface.co/datasets/Sagicc/postocr-sr)

Sources (text):
* PDF files with text overlay, made in digitization process - contain RAW OCR
* tei_xml files with CORRECTED text

(alto_xml - SOON)

Text are novels, and this is a part of "Distant Reading for European Literary History" Project - [link](https://www.distant-reading.net)

More about content and project on the Dataset Card.

### Prerequisite
1. Collect raw ocr material in raw_dir
2. Collect corrected material in corrected_dir

NOTE: If you have corrected text in .txt format skip xml conversion.

### Install packages

1. Create a folder and download this repo

```bash
git clone https://github.com/DigitLib/ocr-correction.git
```
```bash
cd ocr-correction
```

2. Create venv
```bash
python -m venv .venv
```
3. Install packages
```bash
source .venv/bin/activate
```
(.venv) $
```bash
pip install pypdf2 lxml
```

### Extract text

From PDF use [01-convert-pdf.py](01-convert-pdf.py)

From TEI xml use [02-convert-xml.py](02-convert-xml.py)

NOTE: Lines can be different in extracted text, maybe you need to merge them into one line only. For this use [03-merge-lines.py](03-merge-lines.py)

### Create a file_list.csv file
1. Export a list of files in dir to .txt file
```bash
ls /path/to/raw/dir > raw.txt
```
```bash
ls /path/to/corr/dir > corr.txt
```
2. Open an empty spreadsheet file and copy content from created .txt files in two raws - [see example](file_list.csv)
3. Check that files are correspond in both dirs
4. Create a dataset in jsonl format using [04-create-dataset.py](04-create-dataset.py)
5. Login to your HuggingFace, create a dataset page and upload json file.
6. If you like, create train.jsonl for train splin and test.jsonl for validation split.

**Dataset is visible and usable**

NOTE: Write a correct paths to dirs in files.

**Share a link if you make a new dataset :)**
