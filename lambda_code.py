import boto3
import redis
from decimal import Decimal

def lambda_handler(event, context):
    # Initialize DynamoDB Resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('OpenSkyData')

    # Initialize Redis Client
    redis_host = "aidemocache.iavxgy.clustercfg.use1.cache.amazonaws.com"
    redis_port = 6379  # default Redis port, change if yours is different
    r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    # Fetch data from Redis
    redis_data = r.hgetall('icao24')

    # Convert data to appropriate types for DynamoDB
    # Here, we convert any float to Decimal and handle Infinity and NaN
    for key, value in redis_data.items():
        try:
            value = float(value)
            if value == float('inf') or value == float('-inf') or value != value:  # check for Infinity and NaN
                continue  # skip this key-value pair
            redis_data[key] = Decimal(str(value))
        except ValueError:
            pass  # value is not a float, no conversion needed

    # Update DynamoDB table
    for key, value in redis_data.items():
        # Assuming 'icao24' is the partition key
        update_expression = "SET some_attribute = :val"
        expression_values = {':val': value}

        table.update_item(
            Key={'icao24': key},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values
        )

    return {
        'statusCode': 200,
        'body': 'DynamoDB table updated successfully'
    }
