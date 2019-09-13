# -*- coding: utf-8 -*-
import scrapy


class UfcSpider(scrapy.Spider):
    name = 'ufc'
    allowed_domains = ['sherdog.com']
    start_urls = ['http://sherdog.com/']

    def parse(self, response):
        pass
