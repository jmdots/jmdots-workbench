# Extract settings from pyproject.toml
NAME := $(shell grep '^name =' pyproject.toml | sed -E "s/name = \"(.*)\"/\\1/")
VERSION := $(shell grep '^version =' pyproject.toml | sed -E "s/version = \"(.*)\"/\\1/")

.PHONY: install dev-install test ls dist clean

install: dist
	pip install dist/*.whl

dev-install:
	poetry install

test:
	poetry run pytest tests

ls:
	git ls-files --cached --others --exclude-standard

dist: clean
	poetry build

clean:
	rm -rf ./dist

