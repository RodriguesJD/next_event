from requests_html import HTMLSession

from tool_box import tools

events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
next_event_url = tools.next_event_url(events_page)

# next_events_fighters = tools.fighters_on_card(next_event_url)
# for fight in next_events_fighters:
#     print(fight)

