from requests_html import HTMLSession


def html_session(url):
    session = HTMLSession()
    event_page = session.get(url)
    return event_page


def next_event_url(events_page: object) -> str:
    """
    Parse events page and return the url for the next event.

    :param events_page: HTMLSession() of https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2
    :return even_url: url for the next ufc event.
    """
    upcoming_events = events_page.html.xpath('//*[@id="upcoming_tab"]/table/tr[2]')
    event = upcoming_events[0].html.split("document.location='")[1].split("';")[0]
    event_url = f"https://www.sherdog.com{event}"

    return event_url


def fighters_on_card(event_page: object) -> list:
    """

    Parse event_page and return fighters urls.

    :param event_page: HTMLSession() of then next event url
    :return card: List of fighters urls for all the fighters on the card.
    """
    card = []
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


def fighter_info(fighter_page: object) -> list:
    """

    Parse a fighter's information and return it as a list.

    :param fighter_page: HTMLSession() of the fighters page from sherdog.com
    :return fighter_data: A list of the fighters information.
    """
    fight_page = fighter_page.html.xpath("/html/body/div[2]/div[2]/div[1]")
    name = fight_page[0].html.split('class="fn">')[1].split('</span>')[0]
    age = fight_page[0].html.split('Born: <span itemprop="birthDate">')[1].split('<strong>AGE: ')[1].split('</strong>')[0]
    record = fight_page[0].html.split('<span class="record">')[1].split('</span>')[0]
    birth_place = fight_page[0].html.split("birthplace")

    if 'class="locality"' in birth_place[1]:
        city = fight_page[0].html.split('class="locality">')[1].split('</span>')[0]
    else:
        city = "unknown"

    country = fight_page[0].html.split('<strong itemprop="nationality">')[1].split('</strong>')[0]

    fighter_data = [name, age, record, city, country]

    return fighter_data


def next_ufc_event():
    next_ufc_fight_card = []
    ufc_page = html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_ufc_url = next_event_url(ufc_page)
    # TODO get event date
    next_ufc_page = html_session(next_ufc_url)
    fights = fighters_on_card(next_ufc_page)
    for fight in fights:
        single_fight = []
        for fighter_url in fight:
            fighter_page = html_session(fighter_url)
            fighter_information = fighter_info(fighter_page)
            fighter_information.append(fighter_url)
            single_fight.append(fighter_information)

        next_ufc_fight_card.append(single_fight)

    return next_ufc_fight_card
