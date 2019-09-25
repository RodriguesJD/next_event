from requests_html import HTMLSession

from tool_box import tools
from tool_box import betting_tools


def test_betting_page():
    page = betting_tools.betting_page()
    assert str(type(page)) == "<class 'requests_html.HTMLResponse'>"


def test_next_betting_url():
    betting_page = betting_tools.betting_page()
    betting_events = betting_tools.betting_events(betting_page)
    next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')
    session = HTMLSession()
    assert session.get(next_betting_url).status_code == 200
    assert 'ufc' in next_betting_url


def test_betting_events():
    betting_page = betting_tools.betting_page()
    betting_events = betting_tools.betting_events(betting_page)
    assert isinstance(betting_events, list)
    for event in betting_events:
        assert isinstance(event, str)
        assert 'table-header"><a href=' in event


def test_next_betting_date():
    event_str = "September 16th"
    event_date = betting_tools.next_betting_date(event_str)
    assert isinstance(event_date, str)
    assert event_date == "2019-09-16"


def test_event_id():
    betting_page = betting_tools.betting_page()
    betting_events = betting_tools.betting_events(betting_page)
    next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')
    event_id = betting_tools.event_id(next_betting_url)
    assert isinstance(event_id, str)
    assert int(event_id)


def test_betting_odds():
    betting_page = betting_tools.betting_page()
    betting_events = betting_tools.betting_events(betting_page)
    next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')
    event_id = betting_tools.event_id(next_betting_url)
    event_page = tools.html_session(next_betting_url)
    betting_odds = betting_tools.betting_odds(event_page, event_id)
    for fighter_odds in betting_odds:
        assert isinstance(fighter_odds, list)
        for fight_info in fighter_odds:
            assert isinstance(fight_info, str)

