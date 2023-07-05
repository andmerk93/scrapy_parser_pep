# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PepParseItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    status = scrapy.Field()
