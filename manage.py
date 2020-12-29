#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ


def main():
    # """run env """
    # env = environ.Env(
    #     # set casting, default value
    #     DEBUG=(bool, False)
    # )
    #
    # # reading .env file
    # environ.Env.read_env()
    # """Run administrative tasks."""
    # # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_job.settings.base')
    # if eval(env("dev")):
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_job.settings.dev')
    # else:
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_job.settings.prod')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawl_job.settings.prod')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
