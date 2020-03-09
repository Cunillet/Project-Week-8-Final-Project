from scrapy.crawler import CrawlerProcess
from amazon.spiders.AmazonProductSpider import AmazonProductSpider

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})

process.crawl(AmazonProductSpider)
process.start()