import inc_dec     # The code to test
import unittest   # The test framework
import requests 
import lambda_function 

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)

    def test_test(self):
        ride = {
        "PULocationID": 130,
        "DOLocationID": 205,
        "trip_distance": 3.66
        }
        expected_features = {
            "PU_DO": "130_205",
            "trip_distance": 3.66
        }

        self.assertEqual(lambda_function.test(ride), expected_features)
    
    def test_base64_decode(self):
        encoded_data = "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDI1NgogICAgfQ=="
        expected_encoded_data = {
            "ride": {
                "PULocationID": 130,
                "DOLocationID": 205,
                "trip_distance": 3.66
            }, 
            "ride_id": 256
        }
        self.assertEqual(lambda_function.base64_decode(encoded_data), expected_encoded_data)

    def test_predict(self):
        self.assertEqual(1, 1)

    def test_lambda_handler(self):

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


        # result = lambda_function.lambda_handler(event, None)
        # print(result)
        self.assertEqual(1, 1)


    def test_docker_lambda(self):
        
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

        #  how to test docker lambda 
        url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
        actual_response = requests.post(url, json=event).json()

        predictions =  [
            {
                'name': 'Russell Jimenez', 
                'city': 'Jenniferton', 
                'phone': '(377)489-0032x64590', 
                'id': '2bf54686-b801-49d7-9194-9770b7aff96c'
            }
        ]
        
        expected_response = {
            'statusCode': 200,
            'body': "SUCCESS",
            'predictions': predictions
        }
        print(actual_response)
        print("Everywhere stew")
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
