import xml.etree.ElementTree as ET
import csv


class Converters:

    """
    Method to convert xml data to csv. All elements are transformed.
    param: xml_file, csv_file
    """
    def xml_to_csv_all(self, xml_file: string, csv_file: string):

        # Read xml_file
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_data = file.read()

        # Parse XML data
        root = ET.fromstring(xml_data)

        # Extract column headers
        headers = []
        row_elements = root.find('row')[0]
        for child in row_elements:
            headers.append(child.tag)

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write column headers
            writer.writerow(headers)  

            # Write row data
            for row_element in root.findall('row/row'):
                row_data = []
                for child in row_element:
                    row_data.append(child.text)
                writer.writerow(row_data)

        print(f"All XML data has been converted to CSV and saved as '{csv_file}'.")

    """
    Method to convert xml data to csv. All elements are transformed.
    param: xml_file, csv_file, selected_elements
    """
    def xml_to_csv_selected(self, xml_file: string, csv_file: string, selected_elements: list):

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

if __name__ == '__main__':
    converter = Converters()
    xml_file = 'data/Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.xml'

    csv_file = 'xml to csv files/test_all_data_from_xml.csv'

    selected_csv_file = 'xml to csv files/selected_data_from_xml.csv'
    selected_elements = ['indicator', 'panel', 'panel_num']

    converter.xml_to_csv_all(xml_file, csv_file)
    converter.xml_to_csv_selected(xml_file, selected_csv_file, selected_elements)