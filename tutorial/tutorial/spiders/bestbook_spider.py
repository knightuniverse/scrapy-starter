# -*- coding: utf-8 -*-

import scrapy
import re

class BestbookSpider(scrapy.Spider):
    name = "bestbook"

    def start_requests(self):
        urls = [
            'http://bestcbooks.com/B008RVQMBK/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_details_page)

    def parse_details_page(self, response):
        reg = r'密码：(\w*)'
        password = response.css('blockquote p::text').re_first(reg)

        if password is None:
            password = ''

        yield {
            'title': response.css('h1.entry-title::text').extract_first().encode('utf-8'),
            'catalog': response.css('#catalogue_article code::text').extract_first().encode('utf-8'),
            'download_link': response.css('a[ref="external nofollow"]::attr(href)').extract_first(),
            'password': password,
            'origin': response.url,
        }

