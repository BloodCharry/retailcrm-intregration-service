# RetailCRM Integration Service

REST API сервис для интеграции с RetailCRM (API v5) с базовыми операциями над клиентами и заказами.

## Требования

- Python 3.11
- Poetry
- Docker / docker-compose (для контейнерного запуска)
- GNU Make (для удобного запуска команд)

## Запускать можно с помощью:
[Установка и запуск локально (без Makefile)](README.md#установка-и-запуск-локально-без-makefile)

[Makefile команды](README.md#makefile-команды)

[Запуск в Docker](README.md#запуск-в-docker)

## Установка и запуск локально (без Makefile)

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

## Запуск pre-commit хуков:

```bash
poetry run pre-commit run --all-files
```

## Линтинг (ruff):

```bash
poetry run ruff check app
```

## Автоформатирование (black + ruff --fix):

```bash
poetry run black app
poetry run ruff check app --fix
```

## Проверка типов (mypy):

```bash
poetry run mypy app
```

## Запуск тестов (pytest):

```bash
poetry run pytest -v tests/unit
poetry run pytest -v tests/integration
```

После этого сервис будет доступен по адресу:
http://localhost:8000

Подробнее о доступных командах см. раздел [Makefile команды](README.md#makefile-команды)

## Запуск в Docker

```bash
docker-compose up --build
```

## Тестирование

#### В проекте используются pytest и pytest-asyncio.

**Юнит-тесты** — проверяют отдельные функции и классы без обращения к внешним сервисам.

**Интеграционные тесты** — выполняют реальные запросы к RetailCRM API.

### Для интеграционных тестов необходимо:

Указать корректные значения в .env (RETAILCRM_API_KEY, RETAILCRM_BASE_URL, RETAILCRM_SITE).
Создать хотя бы один реальный товар в каталоге RetailCRM.
Его offer.id нужно прописать в .env как TEST_OFFER_ID.
Без этого тесты на создание заказа и платежа будут падать с ошибкой Offer not found.

## Makefile команды

### В проекте используется Makefile для удобного запуска основных задач:

##### install — установка зависимостей через Poetry

```bash
make install
```

##### — запуск всех pre-commit хуков локально

```bash
make precommit
```

##### lint — проверка кода линтером Ruff

```bash
make lint
```

##### format — автоформатирование кода Black + Ruff

```bash
make format
```

##### typecheck — проверка типов mypy

```bash
make typecheck
```

##### test — запуск тестов pytest

```bash
make test
```

##### run — запуск FastAPI приложения через uvicorn

```bash
make run
```

### Структура проекта

#### app/core — конфигурация, безопасность, middleware, логирование

##### app/main.py — точка входа FastAPI

##### tests/ — тесты (pytest + pytest-asyncio)

##### .pre-commit-config.yaml — хуки для форматирования, линтинга и проверки типов

##### Makefile — удобные команды для локальной разработки

##### Полезные ссылки:

#### Документация по api Retailcrm: https://docs.retailcrm.ru/Developers/API/APIMethods