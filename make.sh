#!/bin/bash
python manage.py migrate
python manage.py makemigrations logs
python manage.py sqlmigrate logs 0001
python manage.py migrate
