FROM python:3.7.1-stretch
LABEL maintainer "ricardobchaves6@gmail.com"

WORKDIR /api

ADD . /api

RUN pip install --upgrade pip==19 && \
    pip install -r requirements_dev.txt
