import datetime
import time
import re


# _RE_COMBINE_WHITESPACE = re.compile(r"(?a:\s+)")

from crawl_job.log.logg import logger


def get_timestamp():
    return round(time.time())


def convert_month_day_year_to_timestamp(month_day_year):
    utc = datetime.datetime.strptime(month_day_year, "%Y-%m-%dT%H:%M:%SZ")
    time_stamp = utc.replace(tzinfo=datetime.timezone.utc).timestamp()
    return int(time_stamp)


def convert_timestamp_in_json_data(data):
    try:
        for json_dict in data['results']:
            create_time = json_dict["create_time"]
            # json_dict["create_time"] = datetime.datetime.fromtimestamp(int(create_time))
            json_dict["create_time"] = calculate_time(create_time)
    except Exception as e:
        logger.warning(e)

    return data


def calculate_time(time_stamp):
    create_time = datetime.datetime.fromtimestamp(int(time_stamp))
    duration = datetime.datetime.now() - create_time
    duration_in_s = duration.total_seconds()
    days = divmod(duration_in_s, 86400)  # Get days (without [0]!)
    hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)  # Use remainder of hours to calc minutes
    # seconds = divmod(minutes[1], 1)  # Use remainder of minutes to calc seconds
    if days == 0:
        if hours == 0:
            return "{minutes} min ago".format(minutes=int(minutes[0]))
        else:
            return "{hours} hours ago".format(hours=int(hours[0]))
    else:
        return "{day} day ago".format(day=int(days[0]))


def get_tag_job(tag_name):
    # beauty_tag_name = str(tag_name).strip().replace("\n", " ")
    # beauty_tag_name = _RE_COMBINE_WHITESPACE.sub(" ", beauty_tag_name)
    # beauty_tag_name.split(" ")
    # return beauty_tag_name
    sentence = re.sub(r"\s+", " ", tag_name, flags=re.UNICODE)
    return sentence


# def get_tag_job(data):
#     for json_dict in data['results']:
#         tag_name = json_dict["tag"]
#         if tag_name is None:
#             continue
#         beauty_tag_name = str(tag_name).strip().replace("\n", " ")
#         beauty_tag_name = _RE_COMBINE_WHITESPACE.sub(" ", beauty_tag_name)
#         json_dict["tag"] = beauty_tag_name
#     return data
