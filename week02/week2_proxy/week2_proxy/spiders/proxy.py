# coding:utf-8
import scrapy
from week2_proxy.items import Week2ProxyItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    # def parse(self, response):
    #     pass
    
    def parse(self, response):
        # print(response.text)
        try:
            result = response.text
            # print(result)
            item = Week2ProxyItem()
            item['result'] = result.replace('"','').replace('\n', '')
        except Exception as e:
            print(e)
        yield item
