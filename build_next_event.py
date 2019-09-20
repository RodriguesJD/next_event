from requests_html import HTMLSession

from tool_box import tools

next_event_url = tools.next_event_url()

next_events_fighters = tools.fighters_on_card(next_event_url)
for fight in next_events_fighters:
    print(fight)

