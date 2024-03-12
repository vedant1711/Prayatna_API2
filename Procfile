web: gunicorn hackathon_api.wsgi:application --log-file - --log-level debug
release: python manage.py makemigrations hackathon && python manage.py migrate hackathon