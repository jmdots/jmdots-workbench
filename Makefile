# Extract settings from pyproject.toml
NAME := $(shell grep '^name =' pyproject.toml | sed -E "s/name = \"(.*)\"/\\1/")
VERSION := $(shell grep '^version =' pyproject.toml | sed -E "s/version = \"(.*)\"/\\1/")

# Define the desired output file names
WHEEL_NAME := $(NAME)-$(VERSION)-py3-none-any.whl
SDIST_NAME := $(NAME)-$(VERSION).tar.gz

.PHONY: install dev-install test ls dist clean

install: dist
	pip install dist/$(SDIST_NAME)

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

