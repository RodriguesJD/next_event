from tool_box import betting_tools
from tool_box import event_tools
from tool_box import tools

betting_page = betting_tools.betting_page()
betting_events = betting_tools.betting_events(betting_page)
next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')
event_id = betting_tools.event_id(next_betting_url)
event_page = tools.html_session(next_betting_url)
betting_odds = betting_tools.betting_odds(event_page, event_id)

for fighter_odds in betting_odds:
    for item in fighter_odds:
        print(item)



# next_event = event_tools.next_ufc_event()
# for fight in next_event:
#     for fighter in fight:
#         print(fighter)
