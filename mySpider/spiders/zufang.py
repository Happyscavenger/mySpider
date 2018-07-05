# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from mySpider.items import MyspiderItem

class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['hz.zu.anjuke.com',"www.anjuke.com"]
    start_urls = ['https://hz.zu.anjuke.com/']

    def parse(self, response):
        area_list = response.xpath("//span[@class='elems-l']/div/a[position()>1]")
        for area in area_list:
            item = MyspiderItem()
            item['area_name'] = area.xpath("./text()").extract_first()
            item['area_href'] = area.xpath("./@href").extract_first()
            # print(item)
            yield scrapy.Request(
                item['area_href'],
                callback= self.parse_detail,
                meta={"item":item},
            )

    def parse_detail(self,response):
        item = response.meta['item']
        detail_list = response.xpath("//div[@class='sub-items sub-level2']/a[position()>1]")
        for detail_area in detail_list:
            item['detail_name'] = detail_area.xpath('./text()').extract_first()
            item['detail_href'] = detail_area.xpath('./@href').extract_first()
            yield scrapy.Request(
                item['detail_href'],
                callback=self.parse_detail_area,
                meta={'item':item}
            )

    def parse_detail_area(self,response):
        item = response.meta['item']
        div_list = response.xpath("//div[@class='list-content']/div[position()>2]")

        for div in div_list:
            house_href_list = div.xpath("./@link").extract()
            for house_href in house_href_list:
                if house_href is not None:
                    item['house_href'] = house_href
                    yield scrapy.Request(
                        item['house_href'],
                        callback=self.house_info,
                        meta={'item':deepcopy(item)}
                    )
        next_url = response.xpath("//a[@class='aNxt']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail_area,
            )


    def house_info(self,response):
        item = response.meta['item']
        house_desc_title = response.xpath("//div[@class='wrapper']/h3/text()").extract_first()
        item['house_title'] = house_desc_title
        li_list = response.xpath("//ul[@class = 'house-info-zufang cf']/li")
        for li in li_list:
            item['house_price'] = li.xpath("./../li[1]/span[1]/em/text()").extract_first()
            item['house_type'] = li.xpath("./../li[2]/span[2]/text()").extract_first()
            item['house_size'] = li.xpath("./../li[3]/span[2]/text()").extract_first()
            item['house_floor'] = li.xpath("./../li[5]/span[2]/text()").extract_first()
            item['house_fit'] = li.xpath("./../li[6]/span[2]/text()").extract_first()
            item['house_addr'] = li.xpath("./../li[8]/a/text()").extract()
        p_list = response.xpath("//div[@class='auto-general']/p")
        for p in p_list:
            item["house_desc"] = p.xpath("./text()").extract_first()
        print(item)
