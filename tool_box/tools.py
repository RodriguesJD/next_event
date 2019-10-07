from requests_html import HTMLSession


def html_session(url):
    session = HTMLSession()
    page = session.get(url)
    return page


def month_str_to_int(month_str):
    months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
              "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    return months[month_str]


