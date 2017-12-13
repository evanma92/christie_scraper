from scrapy import Spider, Item, Field
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
import scrapy

from selenium_christie import required_links


class ChristiesItem(Item):
    artist = Field()
    title = Field()
    price_realised = Field()
    lot_number = Field()
    low_estimate = Field()
    high_estimate = Field()

    medium = Field()
    size = Field()
    year_painted = Field()

    provenance = Field()
    literature = Field()
    exhibited = Field()
    special_notice = Field()


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

        description = response.css("span#main_center_0_lblLotDescription::text").extract()
        item['medium'] = description[-4]
        item['size'] = description[-3]
        item['year_painted'] = description[-2]

        item['provenance'] = response.css("p#main_center_0_lblLotProvenance::text").extract()
        item['literature'] = response.css("p#main_center_0_lblLiterature::text").extract()
        item['exhibited'] = response.css("p#main_center_0_lblExhibited::text").extract()
        item['special_notice'] = response.css("p#main_center_0_lblSpecialNotice::text").extract()



        return item
