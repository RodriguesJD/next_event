import arrow


def event_url(tr):
    lines = tr.split('\n')
    url_line = lines[0]
    url_event_ext = url_line.split("document.location='")[1].split("';")[0]
    url = f"https://www.sherdog.com{url_event_ext}"

    return url


def event_date(tr):
    lines = tr.split('\n')
    date_time = None
    for line in lines:
        if "startDate" in line:
            event_date_parse = line.split('content="')[1].split('">')[0]
            event_time_object = arrow.get(event_date_parse)
            date_time = event_time_object

    return date_time


def soonest_date(odd_date, even_date):
    if odd_date < even_date:
        soonest = "odd"
    else:
        soonest = "even"

    return soonest

