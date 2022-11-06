LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': "%(log_color)s%(levelname)-4s%(reset)s %(asctime)s %(message)s"
        },
        "default": {"format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"}
    },
    "handlers": {
        "console": {
            "formatter": "colored",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {"handlers": ["console"]},
    # 'celery': {
    #     'class': 'logging.handlers.RotatingFileHandler',
    #     'filename': 'celery.log',
    #     'formatter': 'simple',
    #     'maxBytes': 1024 * 1024 * 100
    # },
    "loggers": {
        # 'celery': {
        #   'handlers': ['celery', 'console'],
        # },
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
    }
}
