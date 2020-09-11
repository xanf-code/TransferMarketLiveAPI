#!/bin/bash
# python manage.py flush --noinput
curl https://apitmindia.herokuapp.com/tran/latest


# TRUNCATE TABLE transfermktAPI_transfer CASCADE;