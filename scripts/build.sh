#!/usr/bin/env bash
# run this script: ./run_test.sh 

# # Define a function to handle errors
# handle_error() {
#     echo "An error occurred at line $1"
# }

# # Set up error handling with the trap command
# trap 'handle_error $LINENO' ERR

cd "$(dirname "$0")"/../deployment/streaming/

if [ "${LOCAL_IMAGE_NAME}" == "" ]; then 
    # LOCAL_TAG=`date +"%Y-%m-%d-%H-%M"`
    LOCAL_TAG=v1
    export LOCAL_IMAGE_NAME="stream-model-duration:${LOCAL_TAG}"
    echo "LOCAL_IMAGE_NAME is not set, building a new image with tag ${LOCAL_IMAGE_NAME}"
    # docker build -t ${LOCAL_IMAGE_NAME} .
else
    echo "no need to build image ${LOCAL_IMAGE_NAME}"
fi
