# Djate
| Pronounced "झा"

## What is Djate ?
Djate is a simple but effective django template that's is both beginner friendly but not production ready.


## Purpose
This template is created so that testing some qucikly in django becomes easy and not much tedious. Imagine pip installing rest_api, celery, celery backend, flower, etc when you can do it with one click and 1 command


## Physical Architecture
When you run the following command, following will be setup using docker-compose.

![physcial architecture of Djate](/assets/physical_architecture.png)

### Webserver:
Django based webserver which comes preinstalled with django, django rest framework, drf_yasg and other packages. Please look into [requirements.txt](https://github.com/n1rjal/djate/blob/main/requirements.txt)

### Database:
SQLite is the database of choice here. As I mostly use this repository to test some django assumptions or learn something internal about django.

### Message Queue:
Message queue used here is redis. Redis transport is used for celery in this repo

### Flower:
Flower is a celery monitoring tool. It is used to monitor various aspects of celery tasks and queues
The default authentication used for celery is given below.

> Celery runs on port 7777. Suiiiii

** user: admin **
** password: pswd **

## Code Architecture:
Djate follows the basic django architecture of apps and manage.py living in the same path. Each application has same components like views, models, urls, etc with tasks deinfed for celery inside tasks.py file.
The coding pattern of my choice is to use DRF generics and viewsets


## Contributing:
If you want to contribute here are some things I would want for this repository. Make sure you tick your contribution off when you submit your PR
[] Vote for postgres vs sqlite as default database. [Use this issue](https://github.com/n1rjal/djate/issues/1)
[] Use nginx to wrap django app.
[] Add configuration for process management with systemd
[] Add advanced logging
[] Add security fixes
[] Admin panel fixes
[] Todo app implementation
