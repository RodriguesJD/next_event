from tool_box import betting_tools


def test_betting_page():
    page = betting_tools.betting_page()
    assert str(type(page)) == "<class 'requests_html.HTMLResponse'>"
