#!/usr/bin/env bash
# run this script: ./run_test.sh 

# # Define a function to handle errors
# handle_error() {
#     echo "An error occurred at line $1"
# }

# # Set up error handling with the trap command
# trap 'handle_error $LINENO' ERR

cd "$(dirname "$0")"/../deployment/streaming/

# docker build -t stream-model-duration:v1 .

docker-compose up -d

sleep 3

cd ../../

# black .
pylint --recursive=y . 
pytest -v 

cd deployment/streaming/

docker-compose down
