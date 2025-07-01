#!/bin/sh

# Выполняем миграции только если не переданы другие команды
if [ "$#" -eq 0 ]; then
    echo "Applying database migrations..."
    python manage.py migrate --noinput

    echo "Collecting static files..."
    python manage.py collectstatic --noinput

    echo "Starting server..."
    exec gunicorn monitoring_platform.wsgi:application --bind 0.0.0.0:8000
else
    # Если переданы аргументы - выполняем их
    exec "$@"
fi