from tool_box import betting_tools
from tool_box import event_tools
from tool_box import tools


class NextUfcEvent:
    """
    Gather fight data on the next UFC and compile it with betting odds.
    """

    # list of ufc fights in order from last fight to first fight.
    next_event = event_tools.next_ufc_event()

    # list of betting odds organized by fighters name which is in index[0].
    next_ufc_betting_odds = betting_tools.next_ufc_betting_odds()[0]

    # list of fighters information and there betting odds.
    event_odds = []

    def main(self):

        # TODO remove date from next_event. If date is needed later figure out a different way to pass it.
        line_count = 0
        for fight in self.next_event:
            fight_odds = []  # list of an individual fight in the overall fight card.
            if line_count == 0:
                line_count += 1
            else:
                for fighter in fight:
                    fighter_name = fighter[0]  # this name is derived from the next_event list
                    for odds in self.next_ufc_betting_odds:
                        fighter_name_in_odds = odds[0]  # this name is derived from the next_ufc_betting_odds
                        if fighter_name == fighter_name_in_odds:  # match the fighters event and betting information.
                            # TODO create a func that turn the odds into a list of dicts
                            odds.pop(0)  # Remove the fighters name from the odds var.
                            fighter.insert(5, odds)
                            fight_odds.append(fighter)

                self.event_odds.append(fight_odds)

        return self.event_odds


if __name__ == '__main__':
    NextUfcEvent().main()
