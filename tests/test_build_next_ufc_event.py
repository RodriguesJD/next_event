from build_next_ufc_event import NextUfcEvent


def test_main():
    next_event = NextUfcEvent().main()
    assert isinstance(next_event, list)
    for fight in next_event:
        assert isinstance(fight, list)
        for fighter in fight:
            assert isinstance(fighter, dict)
