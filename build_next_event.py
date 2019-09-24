from tool_box import tools

ufc_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
next_ufc_url = tools.next_event_url(ufc_page)
next_ufc_page = tools.html_session(next_ufc_url)
event_date = tools.next_event_date(next_ufc_page)
print(type(event_date))


