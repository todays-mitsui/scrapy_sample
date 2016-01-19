# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = []

    def __init__(self, settings, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)

        f = open(settings.get("START_URLS"))
        urls = f.readlines()
        f.close()

        # 各要素の末尾についた改行文字 "\n" を削除
        # 空行("\n" だけの行)も削除
        self.start_urls = [url.rstrip("\n") for url in urls if url != "\n"]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(settings = crawler.settings)

    def parse(self, response):
        url   = response.url
        title = response.xpath("//title/text()").extract_first()

        yield {"url": url, "title": title}
