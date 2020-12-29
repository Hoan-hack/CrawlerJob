from .base import *
DEBUG = True

TIME_ZONE = 'Asia/Ho_Chi_Minh'

CRONJOBS = [
    ('*/5 * * * *', 'crawl_job.cron.craw_job_scheduled')
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

import dj_database_url

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
