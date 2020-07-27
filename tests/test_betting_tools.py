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
    assert tools.html_session(next_betting_url).status_code == 200
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
    # HTMLResponse for https://www.bestfightodds.com
    betting_page = betting_tools.betting_page()

    # Parse HTMLResponse for all betting events and return the html as a list.
    betting_events = betting_tools.betting_events(betting_page)

    # The first event in the loop will be the next event.
    next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')
    event_id = betting_tools.event_id(next_betting_url)
    event_page = tools.html_session(next_betting_url)
    betting_odds = betting_tools.betting_odds(event_page, event_id)
    for fighter_odds in betting_odds:
        assert isinstance(fighter_odds, list)
        line_count = 0
        for fight_info in fighter_odds:
            if line_count == 0:
                fighter_name = fight_info
                assert isinstance(fighter_name, str)
                line_count += 1
            else:
                assert isinstance(fight_info, dict)
        line_count = 0  # reset line count for the next fighter_odds


def test_next_ufc_betting_odds():
    betting_odds = betting_tools.next_ufc_betting_odds()
    for fighter_odds in betting_odds[0]:
        assert isinstance(fighter_odds, list)
        line_count = 0
        for fight_info in fighter_odds:
            if line_count == 0:
                fighter_name = fight_info
                assert isinstance(fighter_name, str)
                line_count += 1
            else:
                assert isinstance(fight_info, dict)

        line_count = 0  # reset line count for the next fighter_odds

    assert betting_odds[1] == 'ufc'
