FROM python:3-slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install \
  ca-certificates \
  git \
  --no-install-recommends -y

RUN pip install cookiecutter

WORKDIR /app
