FROM python:3

WORKDIR /usr/src/app

ADD ./packages.txt /usr/src/app/packages.txt

RUN pip install -r packages.txt

COPY . /usr/src/app
