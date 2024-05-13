# LOCAL_TAG:=$(shell date +"%Y-%m-%d-%H-%M")
LOCAL_TAG:=v1
LOCAL_IMAGE_NAME:=stream-model-duration:${LOCAL_TAG}
TEST_RUN:=True

setup:
	pip install -r requirements.txt

build: setup 
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/build.sh

run: build
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/run.sh

tests: run
	TEST_RUN=${TEST_RUN} pytest test/

quality_checks: run 
	isort .
	black .
	pylint --recursive=y .
	TEST_RUN=${TEST_RUN} coverage run -m pytest -v
	coverage report -m

publish: quality_checks
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/publish.sh

destroy: 
	LOCAL_IMAGE_NAME=${LOCAL_IMAGE_NAME} bash scripts/destroy.sh

main: publish 
	python main.py