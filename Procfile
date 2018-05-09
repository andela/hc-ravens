web: gunicorn hc.wsgi && ./manage.py ensuretriggers && ./manage.py sendalerts && ./manage.py sendreports
release: python manage.py migrate