import os
import json
import uuid
from time import sleep

import boto3
from faker import Faker

MY_STREAM_NAME = "ride_events"

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
kinesis_client = boto3.client(
    "kinesis",
    region_name="us-east-1",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
faker = Faker()

for i in range(1, 20):
    json_data = {
        "name": faker.name(),
        "city": faker.city(),
        "phone": faker.phone_number(),
        "id": uuid.uuid4().hex,
    }
    print(json_data)
    sleep(0.5)

    put_response = kinesis_client.put_record(
        StreamName=MY_STREAM_NAME, Data=json.dumps(json_data), PartitionKey="name"
    )
    print(put_response)
