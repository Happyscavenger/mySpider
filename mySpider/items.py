# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area_name = scrapy.Field()
    area_href = scrapy.Field()
    detail_name = scrapy.Field()
    detail_href = scrapy.Field()
    house_href = scrapy.Field()
    house_title = scrapy.Field()
    house_price = scrapy.Field()
    house_type = scrapy.Field()
    house_size = scrapy.Field()
    house_floor = scrapy.Field()
    house_fit = scrapy.Field()
    house_addr = scrapy.Field()
    house_desc = scrapy.Field()


class BhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h_title = scrapy.Field()
    h_e_desc = scrapy.Field()
    h_price = scrapy.Field()
    h_href = scrapy.Field()
    h_type = scrapy.Field()
    h_addr = scrapy.Field()
    h_detail_info = scrapy.Field()
    h_master = scrapy.Field()
    h_detail_addr = scrapy.Field()
    h_telephone = scrapy.Field()
    h_detail_fac = scrapy.Field()
    h_detail_type = scrapy.Field()
    content_img = scrapy.Field()

class HouseDay(scrapy.Item):
    area = scrapy.Field()
    area_href = scrapy.Field()
    house_title = scrapy.Field()
    house_href = scrapy.Field()
    house_price = scrapy.Field()
    house_info = scrapy.Field()
    house_addr = scrapy.Field()
    img = scrapy.Field()
    house_desc = scrapy.Field()