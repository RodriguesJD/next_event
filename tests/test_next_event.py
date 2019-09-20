import requests

from tool_box import tools


def test_html_session():
    session = tools.html_session("https://www.sherdog.com/events/UFC-Fight-Night-159-Rodriguez-vs-Stephens-76587")
    assert session.status_code == 200


def test_next_event_url():
    event_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_event_url = tools.next_event_url(event_page)
    domain = 'https://www.sherdog.com'
    assert domain in next_event_url

    assert requests.get(next_event_url).status_code == 200


def test_fighters_on_card():
    events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_fight_url = tools.next_event_url(events_page)
    event_page = tools.html_session(next_fight_url)
    fights = tools.fighters_on_card(event_page)
    for fight in fights:
        for fighters_url in fight:
            assert requests.get(fighters_url).status_code == 200