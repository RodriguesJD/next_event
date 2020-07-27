import pendulum
from requests_html import HTMLSession

from tool_box import tools


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


def next_event_date(event_page: object) -> object:
    """
    Parse event_page and return the date of the next event.

    :param event_page: HTMLSession() of then event page.
    :return event_date: Pendulum datetime object.
    """
    try:
        event = event_page.html.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/header/div/div[2]/div[2]/span[1]/text()')
    except IndexError:
        event = event_page.html.xpath('/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[1]/span[1]/text()')

    event_date_str = event[0]

    year = int(event_date_str.split(", ")[1])

    month_name = event_date_str.split(" ")[0]
    month = tools.month_str_to_int(month_name)

    day = int(event_date_str.split(" ")[1].replace(",", ""))

    event_date = pendulum.datetime(year, month, day)
    return event_date.to_date_string()

class FightersOnCard:
    """
    Parse a sherdog.com fight card. The fights are organized in a lateral fashion. The person on the left is fighting
    the person directly to the right of them. This class returns a nested list. Each nested list contains a fight.

    """
    def __init__(self, event_page):
        self.event_page = event_page

    def fight_is_today(self):
        """
         If the fight is today then the html has a tbody tag to the code that is otherwise not there. I think this is
         because it adds "YET TO COME next to each fighter on the webpage."
        to the html.
        :return:
        """
        html_tbody_tag = self.event_page.html.xpath(
            '/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tbody/tr[2]/td[1]')
        if html_tbody_tag:
            fight_today = True
        else:
            fight_today = False

        return fight_today

    def number_of_fights_in_event(self):
        """
        This looks at the left column and sums up the number of rows in a table. Each row represents a fight excluding
        the main event.
        :return:
        """
        if self.fight_is_today():
            # Day of the event the html changes to say "YET TO COME" next to each fighter
            number_of_fights_left = int(self.event_page.html.xpath(
                '/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tbody/tr[2]/td[1]')[0].text)
        else:
            number_of_fights_left = int(self.event_page.html.xpath(
                '/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[2]/td[1]')[0].text)

        return number_of_fights_left

    def main_event_left(self):
        main_event_left = self.event_page.html.xpath(
            '/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[1]/a')
        main_left = str(main_event_left[0]).split("href='")[1].split("' itemprop='url'>")[0]
        main_left_fighter_url = f"https://www.sherdog.com{main_left}"
        return main_left_fighter_url

    def main_event_right(self):
        main_event_right = self.event_page.html.xpath(
            '/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[2]/a')
        main_right = str(main_event_right[0]).split("href='")[1].split("' itemprop='url'>")[0]
        main_right_fighter_url = f"https://www.sherdog.com{main_right}"

        return main_right_fighter_url

    def fights_on_the_left(self):
        """
        An ordered list of all fights on the left excluding the main event.
        :return:
        """
        list_of_left_fighters = []

        for tr_number in range(2, self.number_of_fights_in_event() + 2):

            if self.fight_is_today():
                left_fighter = self.event_page.html.xpath(
                    f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tbody/tr[{tr_number}]/td[2]')
            else:
                left_fighter = self.event_page.html.xpath(
                    f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[{tr_number}]/td[2]')

            if left_fighter:
                l_fighter = left_fighter[0].html.split('href="/fighter/')[1].split('"><span')[0]
                left_fighter_url = f"https://www.sherdog.com/fighter/{l_fighter}"
                list_of_left_fighters.append(left_fighter_url)

        return list_of_left_fighters

    def fights_on_the_right(self):
        """
        An ordered list of all fights on the right excluding the main event.
        :return:
        """
        list_of_right_fighters = []

        for tr_number in range(2, self.number_of_fights_in_event() + 2):
            if self.fight_is_today():
                right_fighter = self.event_page.html.xpath(
                    f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tbody/tr[{tr_number}]/td[4]')
            else:
                right_fighter = self.event_page.html.xpath(
                    f'/html/body/div[2]/div[2]/div[1]/section[2]/div/div/table/tr[{tr_number}]/td[4]')

            if right_fighter:
                r_fighter = right_fighter[0].html.split('href="/fighter/')[1].split('"><span')[0]
                right_fighter_url = f"https://www.sherdog.com/fighter/{r_fighter}"
                list_of_right_fighters.append(right_fighter_url)

        return list_of_right_fighters

    def main(self):
        fight_card = []
        # Collect the main event and append it to the fight_card list.
        fight_card.append([self.main_event_left(), self.main_event_right()])

        left_fights = self.fights_on_the_left()
        right_fights = self.fights_on_the_right()

        for fight_number in range(0, (self.number_of_fights_in_event() - 1)):
            fight_card.append([left_fights[fight_number], right_fights[fight_number]])

        return fight_card


def fighter_info(fighter_page: object) -> dict:
    """

    Parse a fighter's information and return it as a list.

    :param fighter_page: HTMLSession() of the fighters page from sherdog.com
    :return fighter_data: A list of the fighters information.
    """
    fight_page = fighter_page.html.xpath("/html/body/div[2]/div[2]/div[1]")
    name = fight_page[0].html.split('class="fn">')[1].split('</span>')[0]
    try:
        age = fight_page[0].html.split('Born: <span itemprop="birthDate">')[1].split('<strong>AGE: ')[1].split('</strong>')[0]
    except IndexError:
        age = "N/A"
    record = fight_page[0].html.split('<span class="record">')[1].split('</span>')[0]
    birth_place = fight_page[0].html.split("birthplace")

    if 'class="locality"' in birth_place[1]:
        city = fight_page[0].html.split('class="locality">')[1].split('</span>')[0]
    else:
        city = "unknown"
    country = fight_page[0].html.split('<strong itemprop="nationality">')[1].split('</strong>')[0]

    fighters_info = {"name": name,
                     "age": age,
                     "record": record,
                     "city": city,
                     "country": country}

    return fighters_info


def next_ufc_event() -> dict:
    """
    Collect data on the next ufc event.

    :return next_ufc_fight_card:
    """

    next_ufc_fight_card = []
    ufc_page = tools.html_session("https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2")
    next_ufc_url = next_event_url(ufc_page)
    next_ufc_page = tools.html_session(next_ufc_url)
    next_ufc_dict = {"event_date": next_event_date(next_ufc_page)}
    # TODO add promotion to dict
    fights = FightersOnCard(next_ufc_page).main()

    for fight in fights:
        single_fight = []
        for fighter_url in fight:
            fighter_page = tools.html_session(fighter_url)
            fighter_information = fighter_info(fighter_page)
            fighter_information["fighter_url"] = fighter_url
            single_fight.append(fighter_information)

        next_ufc_fight_card.append(single_fight)

    next_ufc_dict["fights"] = next_ufc_fight_card

    return next_ufc_dict
