FROM python:3.11-slim AS base

ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

COPY pyproject.toml README.md ./

RUN poetry install --no-interaction --no-ansi --without dev

COPY app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
