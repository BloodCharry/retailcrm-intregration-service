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

### Примечание: 
**для docker настроено прооксирование через nginx, все эндпоинты доступны по адресу http://localhost**


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
#### После запуска все сервисы доступны через Nginx по адресу http://localhost:

- API эндпоинты: http://localhost/api/v1/...
- Документация Swagger: http://localhost/docs
- Health-check: http://localhost/healthz

#### Метрики FastAPI (Prometheus формат): http://localhost/metrics
- Prometheus UI: http://localhost/prometheus/
- Grafana UI: http://localhost/grafana/
- 
**После `docker-compose up` дождитесь, пока контейнер `grafana` завершит миграции и станет доступен по адресу http://localhost/grafana/.**

## Дополнительно: Документация через Docusaurus (опционально)
### Установка 
```bash
cd docs-site
npm install
 ```
### запуск документации 
```bash
npm run start
```
### документация будет доступна по адресу: http://localhost:3001/api
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

## API эндпоинты

| Метод | Путь                        | Назначение                                                   |
|-------|-----------------------------|--------------------------------------------------------------|
| GET   | /api/v1/customers           | Получение списка клиентов (фильтры: name, email, registered_from/to) |
| POST  | /api/v1/customers           | Создание нового клиента                                      |
| GET   | /api/v1/customers/{id}/orders | Получение заказов клиента                                   |
| POST  | /api/v1/orders              | Создание нового заказа                                       |
| POST  | /api/v1/payments            | Создание и привязка платежа к заказу                        |
| GET   | /health                     | Health-check                                                 |

**Важно:** при проверке эндпоинта `/api/v1/payments` необходимо указывать реально существующий идентификатор заказа (`order.id`, `order.externalId` или `order.number`).  
Если указать несуществующий ID, RetailCRM вернёт ошибку `400 Bad Request` с сообщением `"Order with {id: ...} does not exist."`.

## Примеры curl

```bash
# Получение списка клиентов
curl -H "X-API-KEY: $API_KEY" http://localhost:8000/api/v1/customers

# Создание клиента
curl -X POST http://localhost:8000/api/v1/customers \
  -H "X-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"firstName": "Иван", "email": "ivan@example.com", "phone": "+79991234567"}'

# Получение заказов клиента
curl -H "X-API-KEY: $API_KEY" http://localhost:8000/api/v1/customers/123/orders

# Создание нового заказа
curl -X POST http://localhost:8000/api/v1/orders \
  -H "X-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "number": "ORD-001",
    "customer_id": 123,
    "items": [
      {"offer_id": 1, "quantity": 2, "price": "99.99"}
    ]
  }'
  
# Создание и привязка платежа к заказу
curl -X POST http://localhost:8000/api/v1/payments \
  -H "X-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": "99.99",
    "type": "bank-card",
    "order": { "id": 456 }
  }'

# фильтрация по имени
curl -G -H "X-API-KEY: $API_KEY" \
  --data-urlencode "filter[firstName]=Иван" \
  http://localhost:8000/api/v1/customers


# фильтрация по email
curl -H "X-API-KEY: $API_KEY" \
  "http://localhost/api/v1/customers?filter%5Bemail%5D=alice@example.com"

# фильтрация по диапазону дат
curl -H "X-API-KEY: $API_KEY" \
  "http://localhost/api/v1/customers?filter%5BcreatedAtFrom%5D=2025-01-01&filter%5BcreatedAtTo%5D=2025-12-31"

```

## Swagger / OpenAPI
**Документация доступна автоматически:**

- Swagger UI: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json

## Переменные окружения (.env) смотрите пример .env.example

- RETAILCRM_API_KEY — API ключ RetailCRM
- RETAILCRM_BASE_URL — базовый URL API (например https://demo.retailcrm.ru/api/v5)
- RETAILCRM_SITE — код сайта в RetailCRM
- TEST_OFFER_ID — ID тестового товара для интеграционных тестов
- PROMETHEUS_PORT=9090
- GRAFANA_PORT=3000
- GRAFANA_ADMIN_USER=admin
- GRAFANA_ADMIN_PASSWORD=admin
- GRAFANA_LOG_LEVEL=warn
- GRAFANA_ANONYMOUS_ENABLED=true
- GRAFANA_ANONYMOUS_ROLE=Admin

### Архитектура проекта

- app/core — конфигурация, логирование, middleware, безопасность
- app/crm — клиент RetailCRM (httpx + логирование)
- app/services — бизнес-логика (customers, orders, payments)
- app/schemas — Pydantic-модели для API
- app/api/v1/routers — FastAPI роутеры
- tests/ — unit + integration тесты

## Наблюдаемость
- Логи в JSON через structlog
- Request ID в каждом запросе (X-Request-ID)
- Health-check доступен по /health

## Безопасность
- Все эндпоинты защищены заголовком X-API-KEY
- Ошибки RetailCRM логируются с деталями запроса/ответа

##### Полезные ссылки:

#### Документация по api Retailcrm: https://docs.retailcrm.ru/Developers/API/APIMethods