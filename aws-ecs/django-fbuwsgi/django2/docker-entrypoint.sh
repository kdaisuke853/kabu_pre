#!/bin/sh

#while :
#do
#  if python /code2/manage.py makemigrations; then
#    break
#  else
#    sleep 1
#  fi
#done

while :
do
  if python /code2/manage.py migrate; then
    break
  else
    sleep 1
  fi
done

#uwsgi --ini /code/$app/$app/uwsgi.ini
#python manage.py runserver 0:8010
uwsgi --socket :8001 --wsgi-file /code2/drfapi/wsgi.py

exit 0