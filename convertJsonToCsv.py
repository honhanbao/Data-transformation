import json
import csv

# XML data
json_file = 'data/Obesity_among_children_and_adolescents_aged_2_19_years__by_selected_characteristics_United_States.json'
# Create CSV file
csv_file = 'json to csv files/all_data_from_json.csv'


# Open the JSON file and load the data into the variable 'data'
with open(json_file) as file:
    data = json.load(file)

# Generate headers of CSV file
header = [item['name'] for item in data['meta']['view']['columns'][8:24]]
# print(header)

# Extract the relevant data rows/entries from the JSON structure
rows = data['data']
rows_data = [row[8:24] for row in rows]
print(rows_data[0])

# Specify the output CSV file path
output_path = csv_file

# Write the data to the CSV file
with open(output_path, 'w', newline='') as file:
    # create the csv writer object
    writer = csv.writer(file)
    # Writing header to CSV file
    writer.writerow(header)
    # Writing data rows to CSV file
    writer.writerows(rows_data)

print(f"All data from JSON file successfully converted to CSV. Saved as '{output_path}'")
