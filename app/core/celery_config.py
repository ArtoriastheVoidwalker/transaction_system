# import os

from .config import settings
# from kombu import Queue

broker_url = f'amqp://{settings.BROKER_USER}:{settings.BROKER_PASSWORD}@{settings.BROKER_HOST}//'
imports = (
    'app.core.celery_app',
    # 'app.celery_tasks.notifications',
    # 'app.celery_tasks.conversations',
    # 'app.celery_tasks.users'
)
result_backend = f'rpc://{settings.BROKER_HOST}:{settings.BROKER_PORT}'
celery_always_eager = True
task_track_started = True
consumer_timeout = False
task_default_queue = 'queue'
broker_transport_options = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
}


# def route_task(name, args, kwargs, options, task=None, **kw):
#     if ":" in name:
#         queue, _ = name.split(":")
#         return {"queue": queue}
#     return {"queue": "celery"}
#
#
# class BaseConfig:
#     CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", broker_url)
#     CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", result_backend)
#
#     CELERY_TASK_QUEUES: list = (
#         # default queue
#         Queue("celery"),
#     )
#
#     CELERY_TASK_ROUTES = (route_task,)
