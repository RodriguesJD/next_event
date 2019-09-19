from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
about = r.html.find('event')



