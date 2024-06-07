from celery import Celery, Task
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.update()


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 5}
    retry_backoff = True
    retry_backoff_max = 60 * 5  # 5 minutes
    retuy_jitter = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)
        self.retry(exc=exc, countdown=60 * 5)


class BaseFor10HoursTask(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 10}
    retry_backoff = True
    retry_backoff_max = 60 * 60 * 10  # 10 hours
    retuy_jitter = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)
        self.retry(exc=exc, countdown=60 * 60 * 10)


class BaseFor24HoursTask(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 60}
    retry_backoff = True
    retry_backoff_max = 60 * 60 * 24  # 10 hours
    retuy_jitter = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)
        self.retry(exc=exc, countdown=60 * 60 * 24)
