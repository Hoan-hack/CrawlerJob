from crawl_job.lib import crawl_job
from apscheduler.schedulers.blocking import BlockingScheduler


# def craw_job_scheduled():
#     crawl_job.get_job_title()


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    crawl_job.get_job_title()


sched.start()
