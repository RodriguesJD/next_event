from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")

e = r.html.xpath('//*[@id="upcoming_tab"]/table')
print(e[0].html)




