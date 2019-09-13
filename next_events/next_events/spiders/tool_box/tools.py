import arrow


def event_url(tr: str) -> str:
    """
    Take html and return a url of a combat event.

    :param tr: html from scrapy spider.
    :return: url: url for the next combat event
    """
    url_event_ext = tr.split("document.location='")[1].split("';")[0]
    url = f"https://www.sherdog.com{url_event_ext}"

    return url


def event_date(tr: str) -> object:
    """
    Take html and return the combat event data as an arrow object.

    :param tr: html from scrapy spider.
    :return: date_time: the date and time of the combat event
    """
    lines = tr.split('\n')
    date_time = None
    for line in lines:
        if "startDate" in line:
            event_date_parse = line.split('content="')[1].split('">')[0]
            event_time_object = arrow.get(event_date_parse)
            date_time = event_time_object

    return date_time


def soonest_date(odd_date: object, even_date: object) -> str:
    """
    Get the odd and even dates to determine what is the next combat event.

    :param odd_date: Arrow object from the odd tags from an events page
    :param even_date: Arrow object from the even tags from an events page
    :return: soonest: odd or even str which is used
    """
    if odd_date < even_date:
        soonest = "odd"
    else:
        soonest = "even"

    return soonest


