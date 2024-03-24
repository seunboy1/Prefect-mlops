import json
import boto3
import base64

kinesis_client = boto3.client('kinesis')

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
        predictions.append(prediction_event)
        print(prediction_event)
        
    
    data_str = json.dumps(predictions)

    # Put the record into the Kinesis stream
    response = kinesis_client.put_record(
        StreamName='ride_predictions',
        Data=data_str,
        PartitionKey=name
    )
    return {
        'statusCode': 200,
        'body': prediction_event
    }
