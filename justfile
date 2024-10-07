#!/usr/bin/env just --justfile

@format: format_html format_py

# Format html
@format_html:
    djlint . --reformat --quiet

# Format Python code
@format_py:
    ruff format
    ruff check --fix

# Lint everything
lint: lint_html lint_py lint_migrations

# Lint HTML
@lint_html:
    djlint . --lint

# Check for missing Django migrations
@lint_migrations:
    python manage.py makemigrations --check --dry-run

# Lint Python code ruff
@lint_py:
    ruff check
    ruff format --check

# Make migrations
@makemigrations:
    python manage.py makemigrations

# Migrate the database
@migrate:
    python manage.py migrate

# Run the development server
@start:
    python manage.py runserver

# Collect static files
@collectstatic:
    python manage.py collectstatic

@push commit_message=":( Enter a real commit message you goof":
    git add .
    git commit -m "{{ commit_message }}"
    git push

@ammend:
    git add .
    git commit --amend --no-edit
    git push --force

# Start the virtual enviroment
@venv:
    source prodev2024/bin/activate

@create_app app_name:
    python manage.py startapp {{ app_name }}

@create_superuser:
    python manage.py createsuperuser
