import requests


ufc_event_url = "https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2"
ufc_event_html = requests.get(ufc_event_url).text

