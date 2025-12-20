.PHONY: install precommit lint format typecheck test run

# Установка зависимостей
install:
	poetry install

# Запуск pre-commit локально
precommit:
	poetry run pre-commit run --all-files

# Линтинг
lint:
	poetry run ruff check app

# Автоформатирование
format:
	poetry run black app
	poetry run ruff check app --fix

# Проверка типов
typecheck:
	poetry run mypy app

# Запуск тестов
test:
	poetry run pytest -v tests/unit
	poetry run pytest -v tests/integration

# Локальный запуск FastAPI
run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
