#!/bin/bash
heroku run python manage.py flush --noinput
#curl https://apitmindia.herokuapp.com/tran/latest