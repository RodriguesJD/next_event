from requests_html import HTMLSession


def html_session(url):
    session = HTMLSession()
    page = session.get(url)
    return page