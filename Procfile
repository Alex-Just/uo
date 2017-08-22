release: python manage.py migrate --noinput
web: gunicorn --backend config.wsgi:application
