#!/bin/bash
git add .
git commit -m "test"
git push heroku master
heroku open
