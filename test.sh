#!/bin/bash
git add .
git commit -m "test"
git push heroku master
#heroku run pipenv install
#heroku run python manage.py migrate
