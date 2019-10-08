

def combine_event_odds(next_event, next_ufc_betting_odds):
    event_odds = []
    for fight in next_event["fights"]:
        fight_odds = []  # list of an individual fight in the overall fight card.
        for fighter in fight:
            fighter_name = fighter["name"]  # this name is derived from the next_event list
            for odds in next_ufc_betting_odds:
                fighter_name_in_odds = odds[0]  # this name is derived from the next_ufc_betting_odds
                if fighter_name == fighter_name_in_odds:  # match the fighters event and betting information.
                    odds.pop(0)  # Remove the fighters name from the odds var.
                    fighter["odds"] = odds
                    fight_odds.append(fighter)

        event_odds.append(fight_odds)

    return event_odds