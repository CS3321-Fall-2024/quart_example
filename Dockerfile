from python:3.11.9-slim-bullseye 

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD_URL=https://install.python-poetry.org
ENV PATH="$PATH:/root/.local/bin"

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests -y \
    curl \
    git \
    bash \
  && curl -sSL $POETRY_DOWNLOAD_URL | python3 - --version $POETRY_VERSION

ENTRYPOINT ["/bin/bash", "-c", "bash"]
