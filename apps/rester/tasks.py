from celery import shared_task
import time

from core.celery import BaseFor10HoursTask


@shared_task(base=BaseFor10HoursTask)
def add_record_for_calculation(n1, n2, res):
    time.sleep(4)
    return f"Calculation for {n1} and {n2} = {res}"
