FROM python:3.11

RUN apt update
RUN apt install -y nano

WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/code
CMD [ "python3", "main.py" ]