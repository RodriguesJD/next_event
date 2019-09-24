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


def test_fighter_info():
    events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_event_url = tools.next_event_url(events_page)
    next_event_page = tools.html_session(next_event_url)
    fights = tools.fighters_on_card(next_event_page)
    for fight in fights:
        for fighter_url in fight:
            fighter_page = tools.html_session(fighter_url)
            fighter_info = tools.fighter_info(fighter_page)
            assert isinstance(fighter_info, list)

            name = fighter_info[0]
            assert isinstance(name, str)

            age = fighter_info[1]
            assert isinstance(age, str)
            assert int(age)

            record = fighter_info[2]
            assert isinstance(record, str)
            record_int_only = record.replace(" ", "").replace("-", "")
            assert int(record_int_only)

            city = fighter_info[3]
            assert isinstance(city, str)

            country = fighter_info[4]
            assert isinstance(country, str)


def test_next_ufc_event():
    next_ufc = tools.next_ufc_event()
    assert isinstance(next_ufc, list)

    for fight in next_ufc:
        assert isinstance(fight, list)
        for fighter in fight:
            assert isinstance(fighter, list)

            name = fighter[0]
            assert isinstance(name, str)

            age = fighter[1]
            assert isinstance(age, str)
            assert int(age)

            record = fighter[2]
            assert isinstance(record, str)
            record_int_only = record.replace(" ", "").replace("-", "")
            assert int(record_int_only)

            city = fighter[3]
            assert isinstance(city, str)

            country = fighter[4]
            assert isinstance(country, str)

            fighters_url = fighter[5]
            assert isinstance(fighters_url, str)
            assert requests.get(fighters_url).status_code == 200
