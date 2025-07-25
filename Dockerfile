FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app/main.py /code/


CMD ["fastapi", "run", "main.py", "--port", "80"]