# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlympicmodelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    nation = scrapy.Field()
    gold = scrapy.Field()
    silver = scrapy.Field()
    bronze = scrapy.Field()
    total = scrapy.Field()
    pass
