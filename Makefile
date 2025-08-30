# Makefile para tareas comunes

.PHONY: up down test lint

up:
	docker compose up -d --build

down:
	docker compose down

test:
	pytest -q

lint:
	ruff .