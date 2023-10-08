FROM python:3.11.5-bookworm

WORKDIR /usr/src/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /usr/src

# install google chrome
RUN apt-get -y update && apt-get install -y gnupg wget

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    && pip3 install --upgrade pip setuptools wheel \
    && pip3 install -r /usr/src/requirements.txt \
    && rm -rf /root/.cache/pip
