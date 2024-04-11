## Streaming using Kinesis

* Creating the role 
* Create a Lambda function, test it
* Create a Kinesis stream
* Connect the function to the stream
* Send the records 

## Code snippets


## Create a Lambda function, test it
### Test event

```json
{
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
```

### Sending this record

```bash
aws kinesis put-record \
    --stream-name ${KINESIS_STREAM_INPUT} \
    --partition-key 1 \
    --data '{
      "name": "Russell Jimenez",
      "city": "Jenniferton",
      "phone": "(377)489-0032x64590",
      "id": "2bf54686-b801-49d7-9194-9770b7aff96c"
    }'
```

### Reading from the stream

```bash
KINESIS_STREAM_OUTPUT='ride_predictions'
SHARD='shardId-000000000000'

SHARD_ITERATOR=$(aws kinesis \
    get-shard-iterator \
        --shard-id ${SHARD} \
        --shard-iterator-type TRIM_HORIZON \
        --stream-name ${KINESIS_STREAM_OUTPUT} \
        --query 'ShardIterator' \
)

RESULT=$(aws kinesis get-records --shard-iterator $SHARD_ITERATOR)

echo ${RESULT} | jq -r '.Records[0].Data' | base64 --decode
``` 


### Running the test

```bash
export PREDICTIONS_STREAM_NAME="ride_predictions"
export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxx
export AWS_DEFAULT_REGION=us-east-1
export TEST_RUN="True"

python test.py
```

### Putting everything to Docker

```bash
docker build -t stream-model-duration:v1 .

docker run -it --rm \
    -p 8080:8080 \
    -e AWS_ACCESS_KEY_ID=AKIA33L6QIYFJDYRZAEO \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e TEST_RUN="True" \
    stream-model-duration:v1
```

URL for testing:

* http://localhost:8080/2015-03-31/functions/function/invocations


### Configuring AWS CLI to run in Docker

To use AWS CLI, you may need to set the env variables:

```bash

    docker run -it --rm \
    -p 8080:8080 \
    -e AWS_ACCESS_KEY_ID=AKIA33L6QIYFJDYRZAEO \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e TEST_RUN="True" \
    stream-model-duration:v1
```

Alternatively, you can mount the `.aws` folder with your credentials to the `.aws` folder in the container:

```bash

    docker run -it --rm \
    -p 8080:8080 \
    -e AWS_ACCESS_KEY_ID=AKIA33L6QIYFJDYRZAEO \
    -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
    -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
    -e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
    -e PREDICTIONS_STREAM_NAME="ride_predictions" \
    -e TEST_RUN="True" \
    -e RUN_ID="e1efc53e9bd149078b0c12aeaa6365df" \
    -v /Users/macbook/.aws :/root/.aws \
    stream-model-duration:v1
```

### Publishing Docker images

Creating an ECR repo

```bash
aws ecr create-repository --repository-name duration-model
```

Logging in

```bash
$(aws ecr get-login --no-include-email)
```

Pushing 

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 814698481162.dkr.ecr.us-east-1.amazonaws.com
docker tag stream-model-duration:v1 814698481162.dkr.ecr.us-east-1.amazonaws.com/duration-model:latest
docker push 814698481162.dkr.ecr.us-east-1.amazonaws.com/duration-model:latest
```
