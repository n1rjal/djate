

init:
    pip freeze | grep poetry || pip install poetry
    source $(poetry env info --path)/bin/activate
    pip install -r requirements.txt
    cp env.example .env
    cp env.example docker.env


create_admin:
    DJANGO_SUPERUSER_USERNAME=$DJANGO_ADMIN_USERNAME DJANGO_SUPERUSER_EMAIL=$DJANGO_ADMIN_EMAIL DJANGO_SUPERUSER_PASSWORD=$DJANGO_ADMIN_PASSWORD python manage.py createsuperuser --noinput


build_dev:
    docker build -f Dockerfile.prod -t djate:dev .


build:
    docker build -f Dockerfile.prod -t djate:latest .

freeze:
    rm requirements.txt
    pip freeze >> requirements.txt

dev:
    python3 manage.py migrate --noinput
    python3 manage.py runserver 0.0.0.0:8000

cleanup:
    docker stop djate_red && docker rm djate_red
    docker stop djate_pg && docker rm djate_pg

prod:
    python3 manage.py migrate --noinput
    python3 manage.py collectstatic --no-input
    just create_admin
    python3 -m gunicorn core.wsgi:application --bind 0.0.0.0:8000 -w 2 --log-level info --access-logfile ./logs/gunicorn.access.log --error-logfile ./logs/gunicorn.error.log
