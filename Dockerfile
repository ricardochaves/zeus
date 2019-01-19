FROM python:3.7.1-stretch
LABEL maintainer "ricardobchaves6@gmail.com"

WORKDIR /base_site

ADD . /base_site

RUN chmod +x ./base_site.sh

RUN pip install --upgrade pip==18.1 && \
    pip install -r requirements_dev.txt
