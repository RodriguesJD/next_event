from requests_html import HTMLSession

# TODO move session and event page to its own function


def html_session(url):
    session = HTMLSession()
    event_page = session.get(url)
    return event_page


def next_event_url(event_page) -> list:
    """
    Parse events page and return the url for the next event.
    :return: url for the next ufc event.
    """
    upcoming_events = event_page.html.xpath('//*[@id="upcoming_tab"]/table/tr[2]')
    event = upcoming_events[0].html.split("document.location='")[1].split("';")[0]
    event_url = f"https://www.sherdog.com{event}"

    return event_url


def fighters_on_card(event_url):
    # TODO create a test for this function
    card = []

    session = HTMLSession()
    event_page = session.get(event_url)
    main_event_left = event_page.html.xpath('/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[1]/a')
    main_left = str(main_event_left[0]).split("href='")[1].split("' itemprop='url'>")[0]
    main_left_fighter_url = f"https://www.sherdog.com{main_left}"

    main_event_right = event_page.html.xpath('/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[2]/a')
    main_right = str(main_event_right[0]).split("href='")[1].split("' itemprop='url'>")[0]
    main_right_fighter_url = f"https://www.sherdog.com{main_right}"

    main_event = [main_left_fighter_url, main_right_fighter_url]

    card.append(main_event)

    number_of_fights_left = int(event_page.html.
                                xpath('/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[2]/td[1]')[0].text)

    for tr_number in range(2, number_of_fights_left + 2):
        left_fighter = event_page.html.xpath(f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[{tr_number}]/td[2]')
        l_fighter = left_fighter[0].html.split('href="/fighter/')[1].split('"><span')[0]
        left_fighter_url = f"https://www.sherdog.com/fighter/{l_fighter}"

        right_fighter = event_page.html.xpath(f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[{tr_number}]/td[4]')
        r_fighter = right_fighter[0].html.split('href="/fighter/')[1].split('"><span')[0]
        right_fighter_url = f"https://www.sherdog.com/fighter/{r_fighter}"

        fight = [left_fighter_url, right_fighter_url]
        card.append(fight)

    return card




