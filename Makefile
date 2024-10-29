init:
	pip freeze | grep poetry || pip install poetry
	# Activate poetry shell
	poetry install || echo "Poetry environment not found."
	# Copy environment files
	cp env.example .env && cp env.example docker.env

create_admin:
	DJANGO_SUPERUSER_USERNAME=$(DJANGO_ADMIN_USERNAME) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_ADMIN_EMAIL) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_ADMIN_PASSWORD) \
	python manage.py createsuperuser --noinput || echo "Superuser creation failed."

build_dev:
	docker buildx build --target development -t djate:dev .

build:
	docker buildx build --target production -t djate:latest .

freeze:
	rm requirements.txt && pip freeze > requirements.txt

dev:
	python manage.py migrate --noinput
	python manage.py runserver 0.0.0.0:8000

cleanup:
	docker stop djate_red || true && docker rm djate_red || true
	docker stop djate_pg || true && docker rm djate_pg || true

prod:
	python manage.py migrate --noinput
	python manage.py collectstatic --no-input --no-post-process
	make create_admin
	python -m gunicorn core.wsgi:application \
		--bind 0.0.0.0:8000 -w 2 --log-level info \
		--access-logfile ./logs/gunicorn.access.log \
		--error-logfile ./logs/gunicorn.error.log
