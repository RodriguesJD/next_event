from pprint import pprint

from tool_box import betting_tools
from tool_box.combine_event_odds import combine_event_odds
from tool_box import event_tools


class NextUfcEvent:
    """
    Gather fight data on the next UFC and compile it with betting odds.
    """

    # list of ufc fights in order from first last fight to first fight.
    next_event = event_tools.next_ufc_event()

    # list of betting odds organized by fighters name which is in index[0].
    next_ufc_betting_odds = betting_tools.next_ufc_betting_odds()[0]

    # combine the fighters info with the fighters betting odds.
    combine_event_odds = combine_event_odds(next_event, next_ufc_betting_odds)

    def main(self):
        next_ufc_event = {"event_date": self.next_event["event_date"],
                          "fights": self.combine_event_odds}

        return next_ufc_event


if __name__ == '__main__':
    ne = NextUfcEvent().main()
    # for fight in ne['fights']:
    #     for fighter in fight:
    #         name = fighter['name']
    #         age = fighter['age']
    #         odds = fighter['odds']
    #         print(name, age)
    #         print(odds)
    #     print("---------------------------------------------------")
    #
    # print(ne)


