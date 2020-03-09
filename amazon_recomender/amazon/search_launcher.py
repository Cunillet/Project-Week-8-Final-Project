"""from scrapy.crawler import CrawlerProcess
from amazon.spiders.AmazonProductSpider import AmazonProductSpider

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data/items.json'
})

process.crawl(AmazonProductSpider)
process.start()
"""
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import scrapy
from scrapy.crawler import CrawlerRunner
from amazon.amazon.spiders.AmazonProductSpider import AmazonProductSpider

def search_products():
    settings = settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/items.json'
    }
    configure_logging(settings=settings)
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(AmazonProductSpider)
        #yield runner.crawl(Spider2)
        reactor.stop()

    crawl()
    reactor.run()