import xml.etree.ElementTree as ET
import csv


# XML data
xml_file = 'data/Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.xml'
# Create CSV file
csv_file = 'xml to csv files/all_data_from_xml.csv'
# xpath parent
xpath_parent = 'row'
# xpath children
xpath_children = 'row/row'
xpath_children_short = './/row'

# Read xml_file
with open(xml_file, 'r', encoding='utf-8') as file:
    xml_data = file.read()

# Parse XML data
root = ET.fromstring(xml_data)

# Extract column headers
headers = []
# row_elements = root.find(xpath_parent)[0]
# row_elements = root.find(xpath_children)
row_elements = root.find(xpath_children_short)
for child in row_elements:
    headers.append(child.tag)

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write column headers
    writer.writerow(headers)  

    # Write row data
    for row_element in root.findall(xpath_children):
        row_data = []
        for child in row_element:
            row_data.append(child.text)
        writer.writerow(row_data)

print(f"All XML data has been converted to CSV and saved as '{csv_file}'.")
