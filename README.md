
### Инструкция по запуску transaction_system на локальном компьютере:

1. Склонировать проект
2. Перейти в директорию проекта
3. Выполнить команду *`python -m venv venv`* для установки виртуального окружения
4. Перейти в виртуальное окружение *`source venv/bin/activate`*
5. Выполнить команду *`pip install -r requirements.txt`*
6. Для применения миграций выполнить команду `./scripts.sh prepare`
7. Для запуска сервера выполнить команду *`./dev.sh`*
8. Для запуска celery-worker  выполнить команду *`celery -A app.worker worker -B -Q queue -c 2 -f celery.logs`*
