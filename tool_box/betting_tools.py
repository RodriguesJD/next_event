import pendulum

from tool_box import tools


def betting_page() -> object:
    """
    HTMLResponse for https://www.bestfightodds.com

    :return page: HTMLResponse for https://www.bestfightodds.com
    """
    page = tools.html_session('https://www.bestfightodds.com')
    return page


def next_betting_url(event_divs, promotion):
    next_event_url = None  # the first event in the loop will be the next event.
    for event in event_divs:
        if promotion in event and not next_event_url:
            event_url_no_domain = event.split('<a href="')[1].split('">')[0]
            event_url = f"https://www.bestfightodds.com{event_url_no_domain}"
            next_event_url = event_url

    return next_event_url


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


def event_id(even_url: str) -> str:
    """
    Parse the event if from the event url
    :param even_url: url of the event
    :return e_id: The events id
    """
    e_id = even_url.split("-")[-1]
    return e_id


def betting_odds(event_page: object, events_id: str) -> list:
    """
    Parse event page for fighters name and there betting odds.

    :param event_page: HTMLResponse of the event page.
    :param events_id: The event id as a string.
    :return event_odds: All the fighters names and there betting odds.
    """
    event_odds = []
    odds_table = event_page.html.xpath(f'//*[@id="event{events_id}"]/div[2]/div[3]/table')
    t = odds_table[0].html.split('<tr')
    for tr_num in range(1, len(t) - 1):
        fighter_odds = []
        name_html = event_page.html.xpath(f'//*[@id="event{events_id}"]/div[2]/div[3]/table/tbody/tr[{tr_num}]/th/a/span')
        if name_html:
            fighter_name = name_html[0].text
            fighter_odds.append(fighter_name)

        betdsi_odds = event_page.html.xpath(f'//*[@id="event{events_id}"]/div[2]/div[3]/table/tbody/tr[{tr_num}]/td[2]/a/span')
        if betdsi_odds:
            betdsi_with_label = {"betdsi": f"{betdsi_odds[0].text}"}
            fighter_odds.append(betdsi_with_label)

        sportsbook_odds = event_page.html.xpath(f'//*[@id="event{events_id}"]/div[2]/div[3]/table/tbody/tr[{tr_num}]/td[7]/a/span')
        if sportsbook_odds:
            sportsbook_with_label = {"sportsbook": f"{sportsbook_odds[0].text}"}
            fighter_odds.append(sportsbook_with_label)

        betonline_odds = event_page.html.xpath(f'//*[@id="event{events_id}"]/div[2]/div[3]/table/tbody/tr[{tr_num}]/td[11]/a/span')
        if betonline_odds:
            betonline_with_label = {"betonline": f"{betonline_odds[0].text}"}
            fighter_odds.append(betonline_with_label)

        if fighter_odds:
            event_odds.append(fighter_odds)

    return event_odds


def next_ufc_betting_odds() -> list:
    """
    Gather the betting odds for the next ufc event.

    :return odds: List of the betting odds for the next ufc event.
    """
    promotion = 'ufc'
    bet_page = betting_page()
    bet_events = betting_events(bet_page)
    next_bet_url = next_betting_url(bet_events, promotion)
    get_event_id = event_id(next_bet_url)
    event_page = tools.html_session(next_bet_url)
    odds = betting_odds(event_page, get_event_id)

    return odds, promotion
