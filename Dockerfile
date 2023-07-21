FROM python:3.11.4

RUN pip install poetry==1.5.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /externalbrowser

COPY pyproject.toml poetry.lock ./
COPY externalbrowser ./externalbrowser
COPY snowflake-connector-python ./snowflake-connector-python

RUN touch README.md

RUN poetry install && rm -rf $POETRY_CACHE_DIR

ENTRYPOINT ["poetry", "run", "python", "externalbrowser/main.py"]
