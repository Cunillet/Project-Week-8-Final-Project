from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import scrapy
from scrapy.crawler import CrawlerRunner
from amazon_details.amazon_details.spiders.AmazonDetailSpider import AmazondetailSpider

def search_product_details():
    settings = settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/items/items.json'
    }
    configure_logging(settings=settings)
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(AmazondetailSpider)
        reactor.stop()

    crawl()
    reactor.run()