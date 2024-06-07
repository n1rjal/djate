#!/bin/sh

cd app
celery -A core flower --port=7777 &
python manage.py runserver 0.0.0.0:8000
