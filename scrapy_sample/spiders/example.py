# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = (
        "http://www.cnn.co.jp/",
        "https://www.yahoo.com/",
        "http://www.reuters.com/"
    )

    def parse(self, response):
        url   = response.url
        title = response.xpath("//title/text()").extract_first()

        yield {"url": url, "title": title}
