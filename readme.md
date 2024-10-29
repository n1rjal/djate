# Djate
| Pronounced झाटे

## What is Djate?
Djate is a simple yet effective Django template that is beginner-friendly and intended for production use and comes with a todo app

## Purpose
The purpose of this template is to simplify testing in Django, making it quick and easy without the hassle of manual setup. Instead of manually installing packages like `django-rest-framework`, `celery`, `celery-backend`, and `flower`, you can get everything up and running with just one click and a single command.

## How to start djate
To get started with djate run just init in the command shell. 
```bash
make init
```

# Physical Architecture
When you run the following command, the setup will be created using `docker-compose`.

![Physical architecture of Djate](/assets/physical_architecture.jpg)

### Webserver:
The webserver is based on Django and comes preinstalled with Django, Django REST framework (DRF), `drf_yasg` for API documentation, and other essential packages. You can find the full list of dependencies in [requirements.txt](https://github.com/n1rjal/djate/blob/main/requirements.txt).

### Database:
The default database used in Djate is SQLite, as it’s lightweight and suitable for quick testing and learning about Django internals. However, there's an open discussion to consider switching to PostgreSQL as the default database.

### Message Queue:
Djate uses Redis as the message queue for Celery. Redis is a popular and efficient transport for managing background tasks in Django.

### Flower:
Flower is included for Celery task monitoring. It allows you to monitor the status of Celery tasks and queues.
Flower runs on port `7777` with the following default credentials:

**Username:** flower_user # look into example.env
**Password:** flower_password # look into example.env

> _Flower runs on port 7777. Suiiiii!_

# Code Architecture:
Djate follows the standard Django project structure with `apps` and `manage.py` in the root directory. Each app has components such as `views.py`, `models.py`, `urls.py`, etc. Celery tasks are defined in `tasks.py` for each application.

The code architecture also leverages Django REST Framework (DRF) generics and viewsets for building APIs efficiently.

## Admin panel
The admin panel here is made using [jazmin-theme](https://django-jazzmin.readthedocs.io/)

![Djate admin panel](/assets/admin-jazzmin.png)

# Production Ready aspects:


## Integration
| Fill in your sentry DSN in env file
- [Sentry](/documents/sentry.md)

## Logging
Logging in this project is done with the following flavor. After you run this project, a logs/ folder will be created. If you are running in production, you will see gunicorn.access.log and guniicorn.error.log files.

### Each log files explained:

1. custom_2024-10-20.log
A time rotated log( 1 day, with retention of 5 days) you can use this for your own cases. Lets say a background worker based task can use this.
```python3
import logging
custom_logger = logging.getLogger("CUSTOM_LOG")
custom_logger.info("INFO MSG")
custom_logger.error("ERROR MSG")
custom_logger.debug("DEBUG MSG")
custom_logger.info("INFO MSG")
custom_logger.critical("CRITICAL MSG")
# and so on
```

2. gunicorn.access.log
When running the server in production, we will see this log, this logs will cntain all the access of the server. Here's an sample example of server access line.
```
127.0.0.1 - - [20/Oct/2024:08:24:47 +0000] "GET /api/v1/todo/tags/list/ HTTP/1.1" 500 145 "http://127.0.0.1:8000/swagger/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
```
You can analyze this log to get info about request response.

3. gunicorn.error.log
Contains error logs as generated from gunicorn.

4. sql_2024-10-20.log
```
2024-10-20 08:39:50,975 [DEBUG] (0.004) SELECT "django_admin_log"."id", "django_admin_log"."action_time", "django_admin_log"."user_id", "django_admin_log"."content_type_id", "django_admin_log"."object_id", "django_admin_log"."object_repr", "django_admin_log"."action_flag", "django_admin_log"."change_message", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined", "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_admin_log" INNER JOIN "auth_user" ON ("django_admin_log"."user_id" = "auth_user"."id") LEFT OUTER JOIN "django_content_type" ON ("django_admin_log"."content_type_id" = "django_content_type"."id") WHERE "django_admin_log"."user_id" = 1 ORDER BY "django_admin_log"."action_time" DESC LIMIT 6; args=(1,); alias=default
```
Use this log to analyze which SQL queries are slow, lagging or learn about if the query used is optimal or not.


## Environment Variables
| Key                     | Description                                                            | Example Value                |
|-------------------------|------------------------------------------------------------------------|------------------------------|
| `CACHE_HOST`            | URL for the Redis cache service.                                       | `redis://localhost:6379/0`   |
| `CELERY_BROKER_URL`     | URL for the Celery message broker, using Redis.                       | `redis://redis:6379/1`      |
| `DB_NAME`               | Name of the PostgreSQL database to connect to.                        | `postgres`                   |
| `DB_USER`               | Username for the PostgreSQL database.                                 | `postgres`                   |
| `DB_PASSWORD`           | Password for the PostgreSQL database user.                            | `postgres`                   |
| `DB_HOST`               | Host address for the PostgreSQL database.                             | `127.0.0.1`                  |
| `DB_PORT`               | Port on which the PostgreSQL database is running.                     | `5432`                       |
| `SENTRY_DSN`            | Data Source Name for Sentry, used for error tracking (leave empty if not used). | ``                      |
| `DJANGO_DEBUG`          | Sets debug mode for Django; use `TRUE` for true, `FALSE` for false.  | `FALSE`                     |
| `DJANGO_ALLOWED_HOSTS`   | Comma-separated list of allowed hostnames for the Django application. | `127.0.0.1,localhost`       |
| `DJANGO_ADMIN_USERNAME`  | Username for the Django admin interface.                              | `djate_admin`               |
| `DJANGO_ADMIN_PASSWORD`  | Password for the Django admin user.                                  | `admin12345`                |
| `DJANGO_ADMIN_EMAIL`     | Email for the Django admin user.                                     | `admin@django.com`          |
| `DOCKERFILE_TARGET`      | Specifies the Dockerfile target environment (development or production). | `development`               |
| `FLOWER_USERNAME`        | Username for accessing the Flower monitoring tool.                   | `flower_user`               |
| `FLOWER_PASSWORD`        | Password for the Flower monitoring tool.                             | `flower_password`           |

## Static files
Static files are served using whitenoise with brotli based compression. Look about it more here
- [Whitenoise](https://whitenoise.readthedocs.io/)
- [Brotli](https://github.com/google/brotli)

## Contributing:
If you want to contribute to Djate, here are some suggestions for improvements. Please check off your contribution when you submit your PR:

- [x] Add Nginx as a reverse proxy for the Django app.
- [x] Implement advanced logging features.
- [x] Apply security fixes.
- [x] Improve the Django admin panel.
- [x] Implement a To-do app as an example project.
- [x] Remove sqlite from repo
- [ ] Implement dockerfile with seperate user
