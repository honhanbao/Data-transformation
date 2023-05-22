import xml.etree.ElementTree as ET
import csv

# XML data
xml_file = 'Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.xml'

with open(xml_file, 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Parse XML data
root = ET.fromstring(xml_data)

# Extract column headers
headers = []
row_elements = root.find('row')[0]

for child in row_elements:
    headers.append(child.tag)

# Create CSV file
csv_file = 'all_data_from_xml.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write column headers

    # Write row data
    for row_element in root.findall('row/row'):
        row_data = []
        for child in row_element:
            row_data.append(child.text)
        writer.writerow(row_data)

    
print(f"XML data has been converted to CSV and saved as '{csv_file}'.")
