FROM python:2 as runtime

RUN pip install pyyaml mapnik

FROM runtime

COPY . /app

WORKDIR /app
