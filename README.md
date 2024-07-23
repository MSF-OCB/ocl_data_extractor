
# OCL concepts and mappings extractor

## Introduction
This Python script extracts cocnepts and mappings from a json file downloaded from OCL.

## Requirements
- Python 3.x
- datetime
- pandas

## Installation
Clone this repository and navigate into the project directory:
```bash
# Clone the script
git clone https://github.com/MSF-OCB/ocl_data_extractor.git
cd ocl_data_extractor
```
## Execution
```bash
# Add your json content to export.json. Ideally this should be the json file in the zipped folder dwoloaded from your versioned collection in OCL.
# ensure you have an updated version of your collection published.

# Downlaod the zip file and extract the json file therein.

# The json file should be names export.json, or copy the files of your json file to the empty export.json file provided.    This is important as the script only parses a file with this name.

# Run the script to generate the excel file witht he errors

py openmrs_logs_translator.py

# You will get an excel output file with concepts on the first sheet and mappings on the other sheet.
```