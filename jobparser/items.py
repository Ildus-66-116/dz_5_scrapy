# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
    description = scrapy.Field()
    number_of_pages = scrapy.Field()
