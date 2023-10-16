FROM python:2 as base

RUN pip install pyyaml mapnik

FROM base

COPY . /usr/src/renderer

WORKDIR /usr/src/renderer
