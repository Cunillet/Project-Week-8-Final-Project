# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.com"]
  
    #Use working product URL below
    ext = input('Searched value: ').replace(' ','+')
    start_urls = [f'https://www.amazon.es/s?k={ext}']
 
    def parse(self, response):
        items = AmazonItem()
        title = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        sale_price = response.xpath('//div[class="a-row a-size-base a-color-base"]/a/text()').extract()
        category = response.xpath('//div[@class="a-row a-size-base a-color-base"]/a/text()').extract()
        reports = response.xpath('//span[@aria-label="31"]/a/span/text()').extract()
        link = response.xpath('//a[@class="a-link-normal a-text-normal"]/@href').extract()
        items['product_name'] = title
        items['product_sale_price'] = sale_price
        items['product_category'] = category
        items['product_reports'] = reports
        items['product_link'] = link
        
        yield items
