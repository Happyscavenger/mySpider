# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        # item['house_desc'] = [re.sub(r'\t', '', i) for i in item['house_desc']]
        return item
