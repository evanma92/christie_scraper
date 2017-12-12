from scrapy import Spider, Item, Field
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
import scrapy

from selenium_christie import required_links
from selenium_sothesby import sothesby_links

class ChristiesItem(Item):
    artist = Field()
    title = Field()
    price_realised = Field()
    lot_number = Field()
    low_estimate = Field()
    high_estimate = Field()

class SothesbyItem(Item):
    artist = Field()
    title = Field()
    price_realised = Field()
    lot_number = Field()
    low_estimate = Field()
    high_estimate = Field()


class ChristiesSpider(Spider):
    name = 'christies'
    allowed_urls = ['http://www.christies.com/']
    start_urls = required_links


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        item = ChristiesItem()
        item['artist'] = response.css("h1.lotName::text").extract()
        item['price_realised'] = response.css("span#main_center_0_lblPriceRealizedPrimary::text").extract()
        item['lot_number'] = response.css("span#main_center_0_lblLotNumber::text").extract()
        item['title'] = response.css("h2 *::text").extract()
        prices = response.css("span#main_center_0_lblPriceEstimatedPrimary::text").extract()[0].split(' - ')
        item['low_estimate'] = prices[0]
        item['high_estimate'] = prices[1]
        return item


class SothesbySpider(Spider):
    name = 'sothesby'
    allowed_urls = ['http://www.sothebys.com/']
    start_urls = sothesby_links


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        item = SothesbyItem()
        item['artist'] = response.css("div.lotdetail-guarantee::text").extract()
        item['price_realised'] = response.css("div.price-sold::text").extract()
        item['lot_number'] = response.css("div.lotdetail-lotnumber::text").extract()
        item['title'] = response.css("div.lotdetail-subtitle::text").extract()
        return item

        




