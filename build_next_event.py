from tool_box import betting_tools
from tool_box import event_tools
from tool_box import tools

# next_ufc = event_tools.next_ufc_event()
# event_date = next_ufc[0]
betting_page = betting_tools.betting_page()
betting_events = betting_tools.betting_events(betting_page)
next_betting_url = betting_tools.next_betting_url(betting_events, 'ufc')



