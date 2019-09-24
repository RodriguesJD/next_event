from tool_box import betting_tools


def test_betting_page():
    page = betting_tools.betting_page()
    assert str(type(page)) == "<class 'requests_html.HTMLResponse'>"


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
