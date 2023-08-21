# DynamoDB Setup
There should be two tables, `aircraftdb` and `etldata`, both have the partition key `icao24`.

# IAM Role Setup
Create a new role with DynamoDB access.

# Create the Lambda Function
* Trigger: DynamoDB Stream aircraftdb
* Role: the one you created above
* Code:

```
import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Initialize tables
aircraftdb = dynamodb.Table('aircraftdb')
etldata = dynamodb.Table('etldata')

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_item = record['dynamodb']['NewImage']
            
            # Extract icao24 from the new item
            icao24 = new_item['icao24']['S']
            
            # Fetch enrichment data from etldata table
            response = etldata.get_item(
                Key={
                    'icao24': icao24
                }
            )
            
            if 'Item' in response:
                enrichment_data = response['Item']
                
                # Update aircraftdb with enrichment data
                aircraftdb.update_item(
                    Key={
                        'icao24': icao24
                    },
                    UpdateExpression="set manufacturericao=:m, registration=:r",
                    ExpressionAttributeValues={
                        ':m': enrichment_data['manufacturericao'],
                        ':r': enrichment_data['registration']
                    },
                    ReturnValues="UPDATED_NEW"
                )

    return {
        'statusCode': 200,
        'body': json.dumps('Data enrichment complete.')
    }
```
