from python:3.11.9-slim-bullseye 

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD_URL=https://install.python-poetry.org
ARG PROJECT_URL=https://github.com/CS3321-Spring-2024/quart_example
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests -y \
    curl \
    git \
    bash \
  && ln -sf /bin/bash /bin/sh \
  && curl -sSL $POETRY_DOWNLOAD_URL | python3 - --version $POETRY_VERSION

WORKDIR /tmp
RUN git clone $PROJECT_URL
WORKDIR /tmp/quart_example

RUN git switch feature/7-gh-actions-workflow \
  && poetry install

EXPOSE 80

CMD ["python", "/tmp/quart_example/src/quart_example/app.py"]
