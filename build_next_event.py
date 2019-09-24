from tool_box import betting_tools
from tool_box import event_tools
from tool_box import tools

# next_ufc = event_tools.next_ufc_event()
# event_date = next_ufc[0]

betting_page = betting_tools.betting_page()
betting_events = betting_tools.betting_events(betting_page)
print(betting_events)

# con = betting_tools.betting_page().html.xpath('//*[@id="content"]')
# divs = con[0].html.split('<div class="')
# for event in divs:
#     if 'table-header"' in event:
#         print('--------------------------------------------------')
#         fight_url_ext = event.split('<a href="')[1].split('">')[0]
#         fight_url = f"https://www.bestfightodds.com/{fight_url_ext}"
#         if 'class="table-header-date">' in event:
#             event_date_str = event.split('class="table-header-date">')[1].split('</span>')[0]
#             event_date = betting_tools.next_betting_date(event_date_str)
#             print(betting_tools.next_betting_event())
#         else:
#             event_date = "unknown"
#         print('--------------------------------------------------')
#     else:
#         pass
#
