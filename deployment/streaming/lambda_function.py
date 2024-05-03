import os
import json
import boto3
import base64


TEST_RUN = os.getenv('TEST_RUN', 'False') == 'True'
PREDICTIONS_STREAM_NAME = os.getenv('PREDICTIONS_STREAM_NAME', 'ride_predictions')

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
kinesis_client = boto3.client('kinesis',
                              region_name='us-east-1',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key
                              )
def base64_decode(encoded_data):
    payload = base64.b64decode(encoded_data)
    event_data = json.loads(payload)

    return event_data

def test(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def lambda_handler(event, context):
    
    predictions =[]
    for record in event['Records']:
        event_data = base64_decode(record['kinesis']['data'])
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
