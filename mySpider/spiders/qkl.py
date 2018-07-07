# -*- coding: utf-8 -*-
import scrapy
# from selenium import webdriver


class QklSpider(scrapy.Spider):
    name = 'qkl'
    allowed_domains = ['weixin.sogou.com','mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/weixin?type=2&query=%E5%8C%BA%E5%9D%97%E9%93%BE']

    def parse(self, response):
        # driver = webdriver.Chrome()
        # driver.get("http://weixin.sogou.com/weixin?type=2&query=%E5%8C%BA%E5%9D%97%E9%93%BE")
        item = {}
        li_list = response.xpath('//ul[@class="news-list"]')
        for li in li_list:
            item['li_href'] = li.xpath('./li//h3/a/@href').extract_first()
            # item['li_titel'] = driver.find_element_by_xpath("./li//h3/")
            yield scrapy.Request(
                item['li_href'],
                callback=self.parse_detail,
                meta={"item":item}
            )

        part_url = "http://weixin.sogou.com/weixin"
        next_url = response.xpath("//a[@id ='sogou_next']/@href").extract_first()
        if next_url is not None:
            next_url = part_url + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

    def parse_detail(self,response):
        item = response.meta['item']
        item['title'] = response.xpath("//div[@id='page-content']//h2/text()").extract_first()
        p_list = response.xpath("//div[@class = 'rich_media_content']/p[position()>1]")
        for p in p_list:
            item['news_info'] = p.xpath(".//text()").extract_first()
            if item['news_info'] is not None:
                item['news_info'] = item['news_info']
        print(item)


























