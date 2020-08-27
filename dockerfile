FROM python:3

RUN mkdir /opt/app
WORKDIR /opt/app

COPY requirements.txt .
COPY source/ ./source/
COPY CBot.py .
COPY config.json .
COPY core.py .

RUN pip3 install -r requirements.txt