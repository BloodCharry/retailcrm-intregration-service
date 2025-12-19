.PHONY: install precommit lint format typecheck test run

# Установка зависимостей
install:
	poetry install

# Запуск pre-commit локально
precommit:
	poetry run pre-commit run --all-files

# Линтинг (ruff)
lint:
	poetry run ruff check app

# Автоформатирование (black + ruff --fix)
format:
	poetry run black app
	poetry run ruff check app --fix

# Проверка типов (mypy)
typecheck:
	poetry run mypy app

# Запуск тестов (pytest)
test:
	poetry run pytest -v

# Локальный запуск FastAPI через uvicorn
run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
