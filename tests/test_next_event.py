import requests

from tool_box import tools


def test_next_event_url():
    next_event_url = tools.next_event_url()
    domain = 'https://www.sherdog.com'
    assert domain in next_event_url

    assert requests.get(next_event_url).status_code == 200
