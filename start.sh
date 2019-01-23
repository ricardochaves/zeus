#!/bin/bash 

export $(egrep -v '^#' .env | xargs)

python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --noinput
python manage.py superuserseed
python manage.py seeddb

#gunicorn -w $GUNICORN_WORKS -b 0.0.0.0:$PORT base_site.wsgi --log-level=debug

python manage.py runserver 0.0.0.0:$PORT

