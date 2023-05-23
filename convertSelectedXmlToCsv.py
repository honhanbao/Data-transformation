import xml.etree.ElementTree as ET
import csv

# XML source file
xml_file = 'data/Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.xml'
# Create CSV output file
csv_file = 'xml to csv files/selected_data_from_xml.csv'
# Select elements to be transformed
selected_elements = ['indicator', 'panel', 'panel_num']

# Read xml_file
with open(xml_file, 'r', encoding='utf-8') as file:
    xml_data = file.read()
    
# Parse XML data
root = ET.fromstring(xml_data)

# Extract column headers
headers = []
row_elements = root.find('row')[0]
for child in row_elements:
    if child.tag in selected_elements:
        headers.append(child.tag)
        # print(child.tag)


with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write column headers
    writer.writerow(headers)  

    # Write row data
    for row_element in root.findall('row/row'):
        row_data = []
        for child in row_element:
            # Note: better to use index
            if child.tag in selected_elements:
                row_data.append(child.text)
                # print(child.text)

        writer.writerow(row_data)
   
print(f"Selected XML data has been converted to CSV and saved as '{csv_file}'.")