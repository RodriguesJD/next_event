from requests_html import HTMLSession

from tool_box import tools


next_event_fight_card = []
events_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
next_event_url = tools.next_event_url(events_page)
next_event_page = tools.html_session(next_event_url)
fights = tools.fighters_on_card(next_event_page)
for fight in fights:
    single_fight = []
    for fighter_url in fight:
        fighter_page = tools.html_session(fighter_url)
        fighter_info = tools.fighter_info(fighter_page)
        single_fight.append(fighter_info)
    next_event_fight_card.append(single_fight)


