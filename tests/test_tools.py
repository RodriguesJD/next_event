from tool_box import tools


def test_html_session():
    session = tools.html_session("https://www.sherdog.com/events/UFC-Fight-Night-159-Rodriguez-vs-Stephens-76587")
    assert session.status_code == 200


def test_month_str_to_int():
    sep = tools.month_str_to_int("Sep")
    assert sep == 9