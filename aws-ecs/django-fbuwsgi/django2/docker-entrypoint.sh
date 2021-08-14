#!/bin/sh


#uwsgi --ini /code/$app/$app/uwsgi.ini
#python manage.py runserver 0:8010
uwsgi --socket :8001 --wsgi-file /code2/drfapi/wsgi.py

exit 0