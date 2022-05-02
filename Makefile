#!/bin/bash
python3 -m venv venv
. venv/bin/activate
export DJANGO_SETTINGS_MODULE=musicProject.settings.local
pip install -r requirements.txt
python manage.py runserver

python manage.py makemigrations

python manage.py migrate

