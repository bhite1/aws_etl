import requests

# Download CSV data
url = "https://opensky-network.org/datasets/metadata/aircraftDatabase.csv"
response = requests.get(url)

if response.status_code == 200:
    csv_data = response.text
    csv_filename = "aircraftDatabase.csv"
    with open(csv_filename, "w") as csv_file:
        csv_file.write(csv_data)
    print(f"CSV data saved to {csv_filename}")
else:
    print("Failed to fetch CSV data.")
