from pprint import pprint

from tool_box import betting_tools
from tool_box import event_tools


class NextUfcEvent:
    """
    Gather fight data on the next UFC and compile it with betting odds.
    """

    # list of ufc fights in order from first last fight to first fight.
    next_event = event_tools.next_ufc_event()

    # list of betting odds organized by fighters name which is in index[0].
    next_ufc_betting_odds = betting_tools.next_ufc_betting_odds()[0]
    # list of fighters information and there betting odds.

    def combine_event_odds(self):
        event_odds = []
        for fight in self.next_event["fights"]:
            fight_odds = []  # list of an individual fight in the overall fight card.
            for fighter in fight:
                fighter_name = fighter["name"]  # this name is derived from the next_event list
                for odds in self.next_ufc_betting_odds:
                    fighter_name_in_odds = odds[0]  # this name is derived from the next_ufc_betting_odds
                    if fighter_name == fighter_name_in_odds:  # match the fighters event and betting information.
                        odds.pop(0)  # Remove the fighters name from the odds var.
                        fighter["odds"] = odds
                        fight_odds.append(fighter)

            event_odds.append(fight_odds)

        return event_odds

    def main(self):
        next_ufc_event = {"event_date": self.next_event["event_date"],
                          "fights": self.combine_event_odds()}

        return next_ufc_event


if __name__ == '__main__':
    NextUfcEvent().main()

