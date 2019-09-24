from tool_box import tools

next_ufc = tools.next_ufc_event()

for fight in next_ufc:
    for fighter in fight:
        print(fighter)


