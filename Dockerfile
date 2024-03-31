FROM python:3.12

COPY ./requirements.txt /code/requirements.txt

COPY ./data /code/data

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

WORKDIR /code/app

# Reload for local development
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
