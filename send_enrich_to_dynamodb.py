import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Load data from JSON file
with open('aircraftDatabase.json', 'r') as file:
        data = json.load(file)

# Iterate through data and prepare items for batch write
batch_items = []
for item in data:
    batch_items.append({
        'PutRequest': {
            'Item': {
                'icao24': {'S': item['icao24']},
                'registration': {'S': item['registration']},
                'model': {'S': item['model']}
                # Add more attributes as needed
            }
        }
    })

# Divide the batch into chunks if needed, as DynamoDB has batch limits
batch_size = 25  # Maximum batch size for batchWriteItem
for i in range(0, len(batch_items), batch_size):
    batch = batch_items[i:i + batch_size]
    response = dynamodb.batch_write_item(RequestItems={'TestEnrichDB': batch})
    print(f'Batch {i//batch_size+1} processed')

print('Data import completed.')
