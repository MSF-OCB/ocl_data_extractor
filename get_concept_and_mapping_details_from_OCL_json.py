"""
Script to extract data from OCL json file in the downloaded zip file
"""
from datetime import datetime
import json
import os
import pandas as pd


def process_json(json_data):
    id_value = json_data.get('id', '')  # Extract id from the main level
    concept_data_list = []
    mapping_data_list = []
    for concept in json_data.get('concepts', []):
        row = {                        
            'ID': concept['id'],
            'ExternalID': concept['external_id'],
            'Source': concept['source'],
            'Collection': id_value,
            'ConceptName': concept['display_name'],
            'Retired': concept['retired']             
        }
        concept_data_list.append(row)
    #return data_list

    for mapping in json_data.get('mappings', []):
            row = {
                'ID': id_value,
                'MappingID': mapping.get('id', ''),
                'MappingExternalID': mapping.get('external_id', ''),
                'MappingSource': mapping.get('source', ''),
                'FromConceptCode': mapping.get('from_concept_code', ''),
                'FromConceptNameResolved': mapping.get('from_concept_name_resolved', ''),
                'ToConceptCode': mapping.get('to_concept_code', ''),
                'ToConceptNameResolved': mapping.get('to_concept_name_resolved', ''),
                'Retired': mapping.get('retired')
            }
            mapping_data_list.append(row)
        
    return concept_data_list, mapping_data_list

def main():
    input_files = ['export.json']  # List of input JSON files
    # Get the current date in the desired format
    current_date = datetime.now().strftime("%d_%b_%Y")
    output_file = f'OCL_Concepts_{current_date}.xlsx'

    concept_data = []
    mapping_data = []
    #combined_data2 = []

    for file in input_files:
        if os.path.exists(file):
            with open(file, 'r') as file:
                json_data = json.load(file)
            concepts, mappings = process_json(json_data)
            concept_data.extend(concepts)
            mapping_data.extend(mappings)
        else:
            print(f"File '{file}' not found. Skipping.")

    # Create DataFrame for concepts data
    df_concepts = pd.DataFrame(concept_data, columns=['ID', 'ExternalID', 'Collection', 'Source', 'ConceptName', 'Retired'])

    # Create DataFrame for mappings data
    df_mappings  = pd.DataFrame(mapping_data, columns=['ID', 'MappingID','MappingExternalID', 'MappingSource', 'FromConceptCode', 'FromConceptNameResolved', 'ToConceptCode', 'ToConceptNameResolved', 'Retired'])

    # Write DataFrames to Excel
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df_concepts.to_excel(writer, sheet_name='Concepts', index=False)
        df_mappings.to_excel(writer, sheet_name='Mappings', index=False)

    print(f'Data written to {output_file}')

if __name__ == "__main__":
    main()
