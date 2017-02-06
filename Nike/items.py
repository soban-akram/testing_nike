# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NikeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    code = scrapy.Field()
    image = scrapy.Field()
    gender = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    product_url = scrapy.Field()
    pass
