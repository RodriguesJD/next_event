from tool_box import betting_tools
from tool_box.combine_event_odds import combine_event_odds
from tool_box import event_tools


def test_combine_event_odds():
    # list of ufc fights in order from first last fight to first fight.
    next_event = event_tools.next_ufc_event()

    # list of betting odds organized by fighters name which is in index[0].
    next_ufc_betting_odds = betting_tools.next_ufc_betting_odds()[0]

    # combine the fighters info with the fighters betting odds.
    event_odds_combined = combine_event_odds(next_event, next_ufc_betting_odds)
    assert isinstance(event_odds_combined, list)
