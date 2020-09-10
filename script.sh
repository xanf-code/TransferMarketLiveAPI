#!/bin/bash
python manage.py flush --noinput
curl http://127.0.0.1:8000/tran/latest