# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonDetailsItem(scrapy.Item):
    product_title = scrapy.Field()
    product_review_count = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_reports = scrapy.Field()
    product_comment_title = scrapy.Field()
    product_comment_body = scrapy.Field()
