import django
django.setup()

import requests
from bs4 import BeautifulSoup

from crawl_job.lib.common.common import convert_month_day_year_to_timestamp, get_timestamp, get_tag_job
from crawl_job.models import models
from crawl_job.log.logg import logger


def get_job_title():
    url = "https://github.com/awesome-jobs/vietnam/issues?page="
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    list_title = []
    for i in range(1, 5):
        rq = requests.get(url + str(i), headers=user_agent, timeout=300)
        soup = BeautifulSoup(rq.text, 'html.parser')
        group = soup.find('div', {"role": "group"})
        tag_id = [tag["id"][6:] for tag in group.select('div[id]')]
        for ids in tag_id:
            try:
                if models.Job.objects.filter(job_id=int(ids)).first():
                    continue
                content = group.find('div', {"id": "issue_" + ids})
                title = content.find('a', {"id": "issue_" + ids + "_link"}).text
                tags = content.find('span', {"class": "labels lh-default d-block d-md-inline"})
                if not tags:
                    tags = None
                else:
                    tags = get_tag_job(tags.text)
                times_tag = content.find('relative-time', {"class": "no-wrap"}).attrs["datetime"]
                create_time = convert_month_day_year_to_timestamp(times_tag)
                update_time = get_timestamp()
                content = get_job_detail(ids)
                if not content:
                    logger.debug('''Can't craw ''' + ids + '''job!''')
                list_title.append({
                    "job_id": ids,
                    "job_detail": title,
                    "tag": tags,
                    "content": str(content),
                    "create_time": create_time,
                    "update_time": update_time
                    }
                )
                list_title = sorted(list_title, key=lambda k: k['job_id'], reverse=True)
            except Exception as e:
                logger.debug(e)
        for job_title in list_title:
            models.Job.objects.update_or_create(**job_title)
    return list_title


def get_job_detail(job_id):

    url_provider = "https://github.com"
    url_detail = "/awesome-jobs/vietnam/issues/"
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = url_provider + url_detail + str(job_id)
    request = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(request.text, 'html.parser')
    table = None
    try:
        table = soup.find('table', {"class": "d-block"})
    except Exception as e:
        logger.debug(e)

    result = table

    return result
