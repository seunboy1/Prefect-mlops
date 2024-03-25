FROM public.ecr.aws/lambda/python:3.9

RUN pip install -U pip
RUN pip install pipenv 

COPY . ./

RUN pip install -r requirements.txt

COPY [ "lambda_function.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]