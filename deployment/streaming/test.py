
import lambda_function

event = {
  "Records": [
    {
      "kinesis": {
        "kinesisSchemaVersion": "1.0",
        "partitionKey": "name",
        "sequenceNumber": "49650427908365418315833497733053628226006584739925852194",
        "data": "eyJuYW1lIjogIlJ1c3NlbGwgSmltZW5leiIsICJjaXR5IjogIkplbm5pZmVydG9uIiwgInBob25lIjogIigzNzcpNDg5LTAwMzJ4NjQ1OTAiLCAiaWQiOiAiMmJmNTQ2ODYtYjgwMS00OWQ3LTkxOTQtOTc3MGI3YWZmOTZjIn0=",
        "approximateArrivalTimestamp": 1711186903.319
      },
      "eventSource": "aws:kinesis",
      "eventVersion": "1.0",
      "eventID": "shardId-000000000002:49650427908365418315833497733053628226006584739925852194",
      "eventName": "aws:kinesis:record",
      "invokeIdentityArn": "arn:aws:iam::814698481162:role/Lamda-kinesis-role",
      "awsRegion": "us-east-1",
      "eventSourceARN": "arn:aws:kinesis:us-east-1:814698481162:stream/youtube-streams"
    }
  ]
}


result = lambda_function.lambda_handler(event, None)
print(result)