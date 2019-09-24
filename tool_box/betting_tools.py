import pendulum

from tool_box import tools


# TODO parse https://www.bestfightodds.com to get betting odds
# TODO get_next_ufc event
# TODO get sportsbook.ag odds
# TODO get betdsi.com odds
# TODO get betonline.ag odds


def betting_page():
    page = tools.html_session('https://www.bestfightodds.com')
    print(type(page))
    return page


def next_event_date(event_str):
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
