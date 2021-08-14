#!/bin/sh

while :
do
  if python /code2/manage.py migrate; then
    break
  else
    sleep 1
  fi
done


uwsgi --socket :8001 --wsgi-file /code2/drfapi/wsgi.py

exit 0