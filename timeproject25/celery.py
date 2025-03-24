from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timeproject25.config.settings")

# install(check_options=True)
app = Celery("timeproject25",
             worker_concurrency=1,
             worker_prefetch_multiplier=1,
             worker_send_task_events=True,
             )
app.config_from_object("django.conf:settings", namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(["timeproject25.tasks"])
