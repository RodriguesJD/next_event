import pendulum

from tool_box import tools


# TODO parse https://www.bestfightodds.com to get betting odds
# TODO get_next_ufc event
# TODO get sportsbook.ag odds
# TODO get betdsi.com odds
# TODO get betonline.ag odds


def betting_page() -> object:
    """
    HTMLResponse for https://www.bestfightodds.com

    :return page: HTMLResponse for https://www.bestfightodds.com
    """
    page = tools.html_session('https://www.bestfightodds.com')
    return page


def betting_events(betting_events_page: object) -> list:
    """
    Parse HTMLResponse for all betting events and return the html as a list.

    :param betting_events_page: HTMLResponse for https://www.bestfightodds.com
    :return events: List of html for each betting events.
    """
    events = []
    content = betting_events_page.html.xpath('//*[@id="content"]')
    event_divs = content[0].html.split('<div class="')
    for event in event_divs:
        if "Future Events" in event:
            pass
        elif 'table-header"' in event:
            events.append(event)

    return events


def next_betting_date(event_str: str) -> str:
    """
    Take the parsed event_str from  https://www.bestfightodds.com and return a pendulum date.

    :param event_str:  parsed event_str from  https://www.bestfightodds.com
    :return event_date.to_date_string(): Pendulum output of the event date
    """
    month_str = event_str.split(" ")[0][:3]
    month = tools.month_str_to_int(month_str)
    day_str = event_str.split(" ")[1]
    if len(day_str) == 3:
        day = int(day_str[:1])
    else:
        day = int(day_str[:2])

    year = 2019

    event_date = pendulum.datetime(year, month, day)

    return event_date.to_date_string()


def next_betting_event(event_str, promotion):
    if "ufc" in event_str:
        print("event_found")