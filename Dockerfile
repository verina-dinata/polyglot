FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./data /code/data

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
