# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiScraperItem(scrapy.Item):
    total_words = scrapy.Field()
    num_links = scrapy.Field()
    num_paragraphs = scrapy.Field()
    percent_as_links = scrapy.Field()
    pass
