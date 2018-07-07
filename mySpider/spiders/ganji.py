# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from selenium import webdriver


class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['www.ganji.com',"sh.ganji.com"]
    start_urls = ['http://sh.ganji.com/fang1']


    def parse(self, response):
        li_list = response.xpath("//div[@class='f-f-content']/dl/dd/div/ul/li[position()>1]")
        for li in li_list:
            item = {}
            item["area_name"] = li.xpath("./a/text()").extract_first()
            item['area_href'] = li.xpath("./a/@href").extract_first()
            part_url = "http://sh.ganji.com"
            item['area_href'] = part_url + item['area_href']
            yield scrapy.Request(
                item['area_href'],
                callback=self.parse_area,
                meta={"item":item}
            )

    def parse_area(self,response):
        item = response.meta["item"]
        div_list = response.xpath("//div[@class='f-list js-tips-list']/div")
        for div in div_list:
            part_url = 'http://sh.ganji.com'
            item['house_href'] = div.xpath("./@href").extract_first()
            item['house_href'] = part_url + urllib.parse.unquote(item['house_href'])
            yield scrapy.Request(
                item["house_href"],
                callback=self.parse_detail,
                meta = {"item":item}
            )
        next_part_url =  response.xpath("//a[@class='next']/@href").extract_first()
        print(next_part_url)
        if next_part_url is not None:
            next_page_num = int(response.xpath("//a[@class='c linkOn']/span/text()").extract_first()) + 1
            next_url = item['area_href'] + "o{}".format(next_page_num)
            print(item['area_href'])
            print(next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_area,
            )


    def parse_detail(self,response):
        item = response.meta['item']
        item['house_title'] = response.xpath("//p[@class='card-title']/i/text()").extract_first()
        item['house_price'] = response.xpath("//ul[@class='card-pay f-clear']/li[@class='price']/span[2]/text()").extract_first()
        item['house_pay_way'] = response.xpath("//ul[@class='card-pay f-clear']/li[@class='type']/text()").extract_first()
        er_list = response.xpath("//ul[@class='er-list-two f-clear']/li")
        for li_l in er_list:
            item["cpd_name"] = li_l.xpath("./../li[1]/span[@class='content']/a/text()").extract_first()
            item["subway-wrap"] = li_l.xpath("./../li[2]/div//text()").extract()
            item["house_addr"] = li_l.xpath("./../li[3]/span/a/text()").extract()
        # chrome_options = Options
        # chrome_options.add_argument("--headless")
        # browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser.get(item["house_href"])
        # item["master_tel"] = browser.find_elements_by_xpath("//div[@class='phone']/a").click()
        # print(type(item["master_tel"]))
        # fireFoxOptions = webdriver.FirefoxOptions()
        # fireFoxOptions.set_headless()
        # browser = webdriver.Firefox(firefox_options=fireFoxOptions)
        # browser.get(item["house_href"])
        # item["master_tel"] = browser.find_elements_by_xpath("//div[@class='phone']/a").click()
        print(item)
        yield item
















