from tool_box import betting_tools


for fights in betting_tools.next_ufc_betting_odds():
    if isinstance(fights, list):
        for fight in fights:
            print(fight)