import xml.etree.ElementTree as ET
import csv

# XML file
xml_file = 'Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.xml'

with open(xml_file, 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Parse XML data
root = ET.fromstring(xml_data)

# Extract column headers
headers = []
row_elements = root.find('row')[0]

for child in row_elements:
    if child.tag == 'indicator':
        headers.append(child.tag)
    if child.tag == 'panel':
        headers.append(child.tag)
    if child.tag == 'panel_num':
        headers.append(child.tag)
    if child.tag == 'unit':
        headers.append(child.tag)
    if child.tag == 'unit_num':
        headers.append(child.tag)
    if child.tag == 'stub_name':
        headers.append(child.tag)
    if child.tag == 'stub_name_num':
        headers.append(child.tag)
    if child.tag == 'stub_label_num':
        headers.append(child.tag)
    if child.tag == 'stub_label':
        headers.append(child.tag)
    if child.tag == 'year':
        headers.append(child.tag)
    if child.tag == 'year_num':
        headers.append(child.tag)
    if child.tag == 'age':
        headers.append(child.tag)
    if child.tag == 'age_num':
        headers.append(child.tag)
    if child.tag == 'estimate':
        headers.append(child.tag)
    if child.tag == 'se':
        headers.append(child.tag)

# Create CSV file
csv_file = 'selected_data_from_xml.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write column headers

    # Write row data
    for row_element in root.findall('row/row'):
        row_data = []
        for child in row_element:
            if child.tag == 'indicator':
                row_data.append(child.text)
            if child.tag == 'panel':
                row_data.append(child.text)
            if child.tag == 'panel_num':
                row_data.append(child.text)
            if child.tag == 'unit_num':
                row_data.append(child.text)
            if child.tag == 'unit':
                row_data.append(child.text)
            if child.tag == 'stub_name':
                row_data.append(child.text)
            if child.tag == 'stub_name_num':
                row_data.append(child.text)
            if child.tag == 'stub_label_num':
                row_data.append(child.text)
            if child.tag == 'stub_label':
                row_data.append(child.text)
            if child.tag == 'year':
                row_data.append(child.text)
            if child.tag == 'year_num':
                row_data.append(child.text)
            if child.tag == 'age':
                row_data.append(child.text)
            if child.tag == 'age_num':
                row_data.append(child.text)
            if child.tag == 'estimate':
                row_data.append(child.text)
            if child.tag == 'se':
                row_data.append(child.text)
        writer.writerow(row_data)
   
print(f"XML data has been converted to CSV and saved as '{csv_file}'.")