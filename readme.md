# Djate
| Pronounced झाटे

## What is Djate?
Djate is a simple yet effective Django template that is beginner-friendly and intended for production use (in future)

## Purpose
The purpose of this template is to simplify testing in Django, making it quick and easy without the hassle of manual setup. Instead of manually installing packages like `django-rest-framework`, `celery`, `celery-backend`, and `flower`, you can get everything up and running with just one click and a single command.

## Physical Architecture
When you run the following command, the setup will be created using `docker-compose`.

![Physical architecture of Djate](/assets/physical_architecture.png)

### Webserver:
The webserver is based on Django and comes preinstalled with Django, Django REST framework (DRF), `drf_yasg` for API documentation, and other essential packages. You can find the full list of dependencies in [requirements.txt](https://github.com/n1rjal/djate/blob/main/requirements.txt).

### Database:
The default database used in Djate is SQLite, as it’s lightweight and suitable for quick testing and learning about Django internals. However, there's an open discussion to consider switching to PostgreSQL as the default database.

### Message Queue:
Djate uses Redis as the message queue for Celery. Redis is a popular and efficient transport for managing background tasks in Django.

### Flower:
Flower is included for Celery task monitoring. It allows you to monitor the status of Celery tasks and queues.
Flower runs on port `7777` with the following default credentials:

**Username:** admin
**Password:** pswd

> _Flower runs on port 7777. Suiiiii!_

## Code Architecture:
Djate follows the standard Django project structure with `apps` and `manage.py` in the root directory. Each app has components such as `views.py`, `models.py`, `urls.py`, etc. Celery tasks are defined in `tasks.py` for each application.

The code architecture also leverages Django REST Framework (DRF) generics and viewsets for building APIs efficiently.

## Contributing:
If you want to contribute to Djate, here are some suggestions for improvements. Please check off your contribution when you submit your PR:

- [ ] Vote for PostgreSQL vs SQLite as the default database. [Use this issue](https://github.com/n1rjal/djate/issues/1)
- [ ] Add Nginx as a reverse proxy for the Django app.
- [ ] Add configuration for process management with Systemd.
- [ ] Implement advanced logging features.
- [ ] Apply security fixes.
- [ ] Improve the Django admin panel.
- [ ] Implement a To-do app as an example project.
