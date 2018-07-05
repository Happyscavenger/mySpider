# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import BhItem
import re


class A58Spider(scrapy.Spider):
    name = '58'
    allowed_domains = ['wh.58.com/chuzu',"jxjump.58.com","short.58.com","m.58.com"," http://m.58.com/wh/zufang"]
    start_urls = ['http://wh.58.com/chuzu/']

    def parse(self, response):
        # 获取５８上武汉的出租房信息
        li_list = response.xpath("//div/ul[@class='list-info hpic']/li")
        for li in li_list:
            item = BhItem()
            item["h_title"] = li.xpath('.//dt/strong/text()').extract_first()
            item['h_title'] = re.sub(r'\xa0',',',item['h_title'])
            item['h_e_desc'] = li.xpath('//dd[1]/span[1]/text()').extract_first()
            item['h_price'] = li.xpath('.//dd[2]/span[1]/text()').extract_first()
            item['h_href'] = li.xpath('./a[1]/@href').extract_first()
            print(item['h_href'])
            yield scrapy.Request(
                item['h_href'],
                callback=self.parse_hours_detail,
                meta= {"item":item}
            )
        # 翻页
        next_url = response.xpath("//div/a[@class='pagenext']/@href").extract_first()
        if next_url:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_hours_detail(self,response):
        item = response.meta['item']
        # h_message = response.xpath('//div[@class="main-wrap"]/div[2]')
        # item["h_pay_way"] = response.xpath('.//span[@class="c_333"]/text()').extract_first()
        item['h_type'] = response.xpath("//ul[@class='houseInfo-detail bbOnepx']/li[1]/i/text()").extract_first()
        item['h_addr'] = response.xpath("//ul[@class='houseInfo-detail bbOnepx']/li[1]/i/text()").extract_first()
        item['h_detail_info'] = response.xpath("//ul[@class='houseInfo-meta bbOnepx']//text()").extract_first()
        item['h_master'] = response.xpath("//div[@class='user']//li/span/text()").extract_first()
        item['h_detail_addr'] = response.xpath('.//li[6]/span[2]/text()').extract_first()
        item['h_telephone'] = response.xpath("//div[@class='user']//li/span/text()").extract()
        item['h_detail_fac'] = response.xpath("//ul[@class='houseDetail-fac']//text()").extract()
        item['h_detail_type'] = response.xpath("//ul[@class='houseDetail-type']//text()").extract()
        # l = []
        # for i in item["h_detail_type"]:
        #     i = re.sub(r'\r','',i)
        #     l.append(i)
        # item["h_detail_type"] = l
        item["content_img"]  = response.xpath("//div[@class='image_area_new']//img/@src").extract()
        item['content_img'] = [i for i in item['content_img']]
        # print(item)
        yield item

