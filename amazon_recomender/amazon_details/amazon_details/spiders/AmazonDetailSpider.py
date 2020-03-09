# -*- coding: utf-8 -*-
import scrapy
from utils.file_utils import obtain_links
from amazon_details.amazon_details.items import AmazonDetailsItem


class AmazondetailSpider(scrapy.Spider):
    name = 'AmazonDetailSpider'
    allowed_domains = ['amazon.com']

    start_urls = [ 'https://www.amazon.es' + link for link in obtain_links('data/items.json') ]

    def parse(self, response):
        items = AmazonDetailsItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        review_count = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract()
        sale_price = response.xpath('//div[@id="priceblock_ourprice"]/a/text()').extract()
        reports = response.xpath('//span[@aria-label="31"]/a/span/text()').extract()
        comment_title = response.xpath('//a[@data-hook="review-title"]/span/text()').extract()
        comment_body = response.xpath('//span[@data-hook="review-body"]/div/div/span/text()').extract()
        items['product_title'] = title.replace('\n','').strip()
        items['product_review_count'] = review_count.replace('\n','').strip()
        items['product_sale_price'] = sale_price.replace('\n','').strip()
        items['product_reports'] = reports.replace('\n','').strip()
        items['product_comment_title'] = comment_title.replace('\n','').strip()
        items['product_comment_body'] = comment_body.replace('\n','').strip()
        
        yield items
