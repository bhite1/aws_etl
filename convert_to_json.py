import csv
import json

csv_filename = "aircraftDatabase.csv"
json_filename = "aircraftDatabase.json"

aircraft_data = []

# Read and parse the CSV file
with open(csv_filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        aircraft_data.append(row)

# Write data to JSON file
with open(json_filename, "w") as json_file:
    json.dump(aircraft_data, json_file, indent=2)

print(f"CSV data converted to JSON and saved to {json_filename}")
