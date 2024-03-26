import os
import json
import boto3
import base64

kinesis_client = boto3.client('kinesis')

TEST_RUN = os.getenv('TEST_RUN', 'False') == 'True'
PREDICTIONS_STREAM_NAME = os.getenv('PREDICTIONS_STREAM_NAME', 'ride_predictions')
# PREDICTIONS_STREAM_NAME = 'ride_predictions'
# TEST_RUN = 'True'

def lambda_handler(event, context):
    
    predictions =[]
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        event_data = json.loads(payload)
        # print("event_data", event_data, type(event_data))
        name = event_data["name"]
        city = event_data["city"]
        phone = event_data["phone"]
        id = event_data["id"]
        
        prediction_event = {
            "name": name,
            "city": city,
            "phone": phone,
            "id": id
        }
    
        data_str = json.dumps(prediction_event)

        # Put the record into the Kinesis stream
        

        if not TEST_RUN:
            kinesis_client.put_record(
                StreamName=PREDICTIONS_STREAM_NAME,
                Data=data_str,
                PartitionKey=name
            )
        
        predictions.append(prediction_event)
    # print(prediction_event)
        
    return {
        'statusCode': 200,
        'body': "SUCCESS",
        'predictions': predictions
    }