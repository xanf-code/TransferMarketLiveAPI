#!/bin/bash
heroku run python manage.py flush --noinput
git add .
git commit -m "new version"
git push heroku master
#curl https://apitmindia.herokuapp.com/tran/latest