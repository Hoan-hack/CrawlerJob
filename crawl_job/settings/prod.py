from .base import *
DEBUG = False

TIME_ZONE = 'Asia/Ho_Chi_Minh'

CRONJOBS = [
    ('*/5 * * * *', 'crawl_job.cron.craw_job_scheduled'),
]

# DATABASES = {
#     'default': {
#
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#
#         'NAME': 'd6bcc0nounn8lj',
#
#         'USER': 'osmlrkzmdcvsha',
#
#         'PASSWORD': '8b85ebd07decac6f46ac11e148abc1369848ae1d6208c897e60345d1ed3087e5',
#
#         'HOST': 'ec2-54-160-133-106.compute-1.amazonaws.com',
#
#         'PORT': '5432',
#
#     }
# }

import dj_database_url

DATABASE_URL = "postgres://osmlrkzmdcvsha:8b85ebd07decac6f46ac11e148abc1369848ae1d6208c897e60345d1ed3087e5@" \
               "ec2-54-160-133-106.compute-1.amazonaws.com:5432/d6bcc0nounn8lj"

# prod_db = dj_database_url.config(default=DATABASE_URL)
# DATABASES['default'].update(prod_db)
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

