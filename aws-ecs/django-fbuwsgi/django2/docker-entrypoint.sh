#!/bin/sh

uwsgi --socket :8001 --wsgi-file /code2/drfapi/wsgi.py

exit 0