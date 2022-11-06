from celery import Celery
from app.core.celery_app import celery_app


def make_celery():
    return celery_app


if __name__ == "__main__":
    make_celery().worker_main()
