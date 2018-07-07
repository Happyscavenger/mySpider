# -*- coding: utf-8 -*-
import scrapy
import urllib
from mySpider.items import HouseDay
class FtxSpider(scrapy.Spider):
    name = 'ftx'
    allowed_domains = ['zu.hz.fang.com']
    start_urls = ['http://zu.hz.fang.com']

    def parse(self, response):
        a_list = response.xpath("//dd[@style='position: relative;']/a[position()>1]")
        item = HouseDay()
        for a in a_list:
            item['area'] = a.xpath("./text()").extract_first()
            item['area_href'] = a.xpath('./@href').extract_first()
            if item['area_href'] is not None:
                item['area_href'] = urllib.parse.urljoin(response.url,item['area_href'])
                yield scrapy.Request(
                    item['area_href'],
                    callback= self.parse_detail,
                    meta={"item":item}
                )

    def parse_detail(self,response):
        item = response.meta['item']
        dl_list= response.xpath("//div[@class='houseList']/dl[position()!=10]")
        for dl in dl_list:
            item['house_title'] = dl.xpath("./dd/p[1]//@title").extract_first()
            item['house_href'] = dl.xpath("./dd/p[1]/a/@href").extract_first()
            if item['house_href'] is not None:
                item['house_href'] = urllib.parse.urljoin(response.url,item['house_href'])
                yield scrapy.Request(
                    item['house_href'],
                    callback=self.parse_house_detail,
                    meta={"item":item}
                )
        next_part_url =  response.xpath('//div[@id="rentid_D10_01"]/a[text()="下一页"]/@href').extract_first()
        if next_part_url is not None:
            next_page_num = int(response.xpath("//div[@class='fanye']/a[@class='pageNow']/text()").extract_first()) + 1
            next_url = item['area_href'] + "i3{}".format(next_page_num)
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail,
            )

    def parse_house_detail(self,response):
        item = response.meta['item']
        div_list = response.xpath("//div[@class='tab-cont-right']/div[position()>1]")
        for div in div_list:
            item['house_price'] = div.xpath("//i/text()").extract_first()
            item['house_info'] = div.xpath("///div[@class='tt']/text()").extract()
            item['house_addr'] = div.xpath("///div[@class='rcont']/a/text()").extract()
        li_list = response.xpath("//div[@class='little-img']/ul/li")
        for li in li_list:
            item['img']=li.xpath("./img/@src").extract_first()
        item['house_desc'] = response.xpath("//ul[@class='fyms_modify']/li/div[2]/text()").extract_first()
        yield item