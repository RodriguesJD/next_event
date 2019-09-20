from requests_html import HTMLSession

from tool_box import tools

events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
next_event_url = tools.next_event_url(events_page)

next_event_page = tools.html_session(next_event_url)

fights = tools.fighters_on_card(next_event_page)


for fight in fights:
    print(fight)

