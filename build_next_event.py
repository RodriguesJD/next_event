from tool_box import event_tools

next_ufc = event_tools.next_ufc_event()
event_date = next_ufc[0]

for fight in next_ufc:
    if fight == event_date:
        # index 0 is the event date
        pass
    else:
        print(fight)
