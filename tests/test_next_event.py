import arrow
import requests

from next_events.next_events.spiders.tool_box import tools


def test_event_url():
    text = """<tr class="odd" onclick="document.location='/events/UFC-Fight-Night-158-Cowboy-vs-Gaethje-76585';" 
    itemscope itemtype="http://schema.org/Event">\n
    <td>\n
    <meta itemprop="startDate" content="2019-09-14T00:00:00-07:00">\n
    <span class="date"><span class="month">Sep</span><span class="day">14</span><span class="year">2019</span></span>\n
    </td>\n
    <td>\n
    <a itemprop="url" href="/events/UFC-Fight-Night-158-Cowboy-vs-Gaethje-76585">\n
    <span itemprop="name">UFC Fight Night 158 - Cowboy vs. Gaethje</span>\n
    </a>\n
    </td>\n
    <td itemprop="location"><img src="https://www3-cdn.sherdog.com/2793/img/flags/ca.gif" width="16" height="11" 
    alt="country"> Rogers Arena, Vancouver, British Columbia, Canada</td>\n
    </tr>"""
    event_url = tools.event_url(text)
    assert event_url
    assert requests.get(event_url).status_code == 200


def test_event_date():
    text = """<tr class="odd" onclick="document.location='/events/UFC-Fight-Night-158-Cowboy-vs-Gaethje-76585';" 
    itemscope itemtype="http://schema.org/Event">\n
    <td>\n
    <meta itemprop="startDate" content="2019-09-14T00:00:00-07:00">\n
    <span class="date"><span class="month">Sep</span><span class="day">14</span><span class="year">2019</span></span>\n
    </td>\n
    <td>\n
    <a itemprop="url" href="/events/UFC-Fight-Night-158-Cowboy-vs-Gaethje-76585">\n
    <span itemprop="name">UFC Fight Night 158 - Cowboy vs. Gaethje</span>\n
    </a>\n
    </td>\n
    <td itemprop="location"><img src="https://www3-cdn.sherdog.com/2793/img/flags/ca.gif" width="16" height="11" 
    alt="country"> Rogers Arena, Vancouver, British Columbia, Canada</td>\n
    </tr>"""

    event_date = tools.event_date(text)
    assert event_date
    assert arrow.get(event_date)



