## Setup Celery
- install redis, celery, django-celery-results, django-celery-beat, eventlet(with windows)
- add file celery.py in setting folder, add setting for celery, for send mail
(DOC: celery: https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
- run celery: celery -A mysite worker -l info --pool=solo (--pool using with windows)
- runserver

-----
## Run celery beat
- run celery: celery -A mysite worker -l info --pool=solo (--pool using with windows)
- run celery-beat: celery -A mysite beat -l info

-----
## Difference between different ways to create celery task: @share_task and @celery.task
- celery v3 -> @celery.task
- celery v4 -> @share_task