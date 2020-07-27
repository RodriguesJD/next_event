import requests

from tool_box import event_tools
from tool_box import tools


def test_next_event_url():
    event_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_event_url = event_tools.next_event_url(event_page)
    domain = 'https://www.sherdog.com'
    assert domain in next_event_url

    assert requests.get(next_event_url).status_code == 200


def test_next_event_date():
    ufc_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_ufc_url = event_tools.next_event_url(ufc_page)
    next_ufc_page = tools.html_session(next_ufc_url)
    event_date = event_tools.next_event_date(next_ufc_page)
    assert isinstance(event_date, str)


def test_fighters_on_card():
    events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_fight_url = event_tools.next_event_url(events_page)
    event_page = tools.html_session(next_fight_url)
    fights = event_tools.FightersOnCard(event_page).main()
    for fight in fights:
        for fighters_url in fight:
            assert requests.get(fighters_url).status_code == 200


def test_fighter_info():
    events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_event_url = event_tools.next_event_url(events_page)
    next_event_page = tools.html_session(next_event_url)
    fights = event_tools.FightersOnCard(next_event_page).main()
    for fight in fights:
        for fighter_url in fight:
            fighter_page = tools.html_session(fighter_url)
            fighter_info = event_tools.fighter_info(fighter_page)
            assert isinstance(fighter_info, dict)

            name = fighter_info["name"]
            assert isinstance(name, str)

            age = fighter_info["age"]
            assert isinstance(age, str)
            assert int(age)

            record = fighter_info["record"]
            assert isinstance(record, str)
            record_int_only = record.replace(" ", "").replace("-", "")
            assert int(record_int_only)

            city = fighter_info["city"]
            assert isinstance(city, str)

            country = fighter_info["country"]
            assert isinstance(country, str)


def test_next_ufc_event():
    next_ufc = event_tools.next_ufc_event()
    assert isinstance(next_ufc, dict)
    for fight in next_ufc["fights"]:
        assert isinstance(fight, list)
        for fighter in fight:
            assert isinstance(fighter, dict)
            name = fighter["name"]
            assert isinstance(name, str)

            age = fighter["age"]
            assert isinstance(age, str)
            assert int(age)

            record = fighter["record"]
            assert isinstance(record, str)
            record_int_only = record.replace(" ", "").replace("-", "")
            assert int(record_int_only)

            city = fighter["city"]
            assert isinstance(city, str)

            country = fighter["country"]
            assert isinstance(country, str)

            fighters_url = fighter["fighter_url"]
            assert isinstance(fighters_url, str)
            assert requests.get(fighters_url).status_code == 200
