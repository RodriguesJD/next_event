# -*- coding: utf-8 -*-
import scrapy
from tool_box import tools


class UfcSpider(scrapy.Spider):
    name = 'ufc'
    allowed_domains = ['sherdog.com']
    start_urls = ['https://www.sherdog.com/organizations/Ultimate-Fighting-Championship-UFC-2']

    def parse(self, response):
        event_table = response.xpath('//table[@class="event"]')
        trs_odd = event_table.xpath('//tr[@class="odd"]')
        trs_even = event_table.xpath('//tr[@class="even"]')
        # trs = trs_even + trs_odd
        next_odd_card = trs_odd.get()
        next_even_card = trs_even.get()

        odd_event_url = tools.event_url(next_odd_card)
        odd_event_date = tools.event_date(next_odd_card)

        even_event_url = tools.event_url(next_even_card)
        even_event_date = tools.event_date(next_even_card)

        odd_or_even = tools.soonest_date(odd_event_date, even_event_date)
        if odd_or_even == "odd":
            next_card = odd_event_url
        else:
            next_card = even_event_url

        yield scrapy.Request(next_card, callback=self.next_card)

    def next_card(self, response):
        main_event_left = response.xpath("/html/body/div[2]/div[2]/div[1]/section[1]/div/div[2]/div[2]/div[1]").get()
        # print(main_event_left)