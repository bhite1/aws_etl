import json

json_filename = "aircraftDatabase.json"

# Read the JSON file
with open(json_filename, "r") as json_file:
        aircraft_data = json.load(json_file)

# Extract specific fields for each set of data
data_fields = ["icao24", "model"]
model_data = [{field: aircraft[field] for field in data_fields} for aircraft in aircraft_data]

data_fields = ["icao24", "owner"]
owner_data = [{field: aircraft[field] for field in data_fields} for aircraft in aircraft_data]

data_fields = ["icao24", "typecode"]
typecode_data = [{field: aircraft[field] for field in data_fields} for aircraft in aircraft_data]

# Write data to individual JSON files
model_filename = "model_data.json"
with open(model_filename, "w") as model_file:
    json.dump(model_data, model_file, indent=2)

owner_filename = "owner_data.json"
with open(owner_filename, "w") as owner_file:
    json.dump(owner_data, owner_file, indent=2)

typecode_filename = "typecode_data.json"
with open(typecode_filename, "w") as typecode_file:
    json.dump(typecode_data, typecode_file, indent=2)

print("Individual JSON files created.")
