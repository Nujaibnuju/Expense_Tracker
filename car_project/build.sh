#!/usr/bin/env bash

# install packages
pip install -r requirements.txt


# database migrate
python manage.py migrate


# collect static files
python manage.py collectstatic --noinput