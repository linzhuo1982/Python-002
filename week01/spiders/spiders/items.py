# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    m_name = scrapy.Field()
    m_type = scrapy.Field()
    m_time = scrapy.Field()