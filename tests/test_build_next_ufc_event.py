from build_next_ufc_event import NextUfcEvent


def test_main():
    next_event = NextUfcEvent().main()
    assert isinstance(next_event, dict)

    event_date = next_event["event_date"]
    assert isinstance(event_date, str)

    for fight in next_event['fights']:
        assert isinstance(fight, list)
        for fighter in fight:
            assert isinstance(fighter, dict)
