release: python manage.py migrate --noinput
web: gunicorn --pythonpath backend config.wsgi:application
