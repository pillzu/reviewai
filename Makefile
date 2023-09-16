.RECIPEPREFIX = >
.ONESHELL:
SHELL := /bin/bash

setup:
> @echo "Creating setup file structure..."
> @pip3 install virtualenv
> @if [ ! -d .venv ]; then\
>   python3 -m venv .venv;\
> fi
> @source .venv/bin/activate
> @pip install -r requirements.txt

export: requirements.txt
> @echo "Exporting requirements.txt"
> @source .venv/bin/activate
> @pip freeze > requirements.txt

install:
> @echo "Installing updated requirements.txt"
> @source .venv/bin/activate
> @pip freeze
> @pip install -r requirements.txt

run: 
> @echo "Starting docker containers..."
> @docker compose up
  

