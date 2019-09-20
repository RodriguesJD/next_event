from requests_html import HTMLSession


def next_event_url() -> list:
    """
    Parse events page and return the url for the next event.
    :return: url for the next ufc event.
    """
    session = HTMLSession()
    event_page = session.get("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    upcoming_events = event_page.html.xpath('//*[@id="upcoming_tab"]/table/tr[2]')
    event = upcoming_events[0].html.split("document.location='")[1].split("';")[0]
    event_url = f"https://www.sherdog.com{event}"

    return event_url
