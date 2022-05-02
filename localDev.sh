#!/bin/bash

# meant for mac and linux users
# be sure to start your local virtual environment with
#  . venv/bin/activate
# then source this file for a quick start-up
export DJANGO_SETTINGS_MODULE=musicProject.settings.local
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
