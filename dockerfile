FROM python:3

RUN mkdir /opt/app
WORKDIR /opt/app

COPY . .

RUN pip3 install -r requirements.txt