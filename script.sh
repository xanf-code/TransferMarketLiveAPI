#!/bin/bash
heroku pg:reset --confirm apitmindia
heroku run python manage.py migrate
# curl https://apitmindia.herokuapp.com/tran/latest
