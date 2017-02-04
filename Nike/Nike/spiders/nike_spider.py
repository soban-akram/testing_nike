import scrapy
from scrapy.http import FormRequest
from scrapy.spiders import Spider 
from scrapy.selector import HtmlXPathSelector
from Nike.items import NikeItem
from scrapy.http import FormRequest, Request
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import json


class NikeCrawler(Spider):
    name = "nike"
    allowed_domains = ["store.nike.com"]

    def start_requests(self):
        product_items = [
            Item('http://store.nike.com/html-services/gridwallData?gridwallPath=mens-basketball-shoes/7puZ8r1Zoi3&country=US&lang_locale=en_US', 'mens', 'shoes', 'basketball'),
            Item('http://store.nike.com/html-services/gridwallData?gridwallPath=mens-lifestyle-shoes/7puZoneZoi3&country=US&lang_locale=en_US', 'mens', 'shoes', 'lifestyle')
        ]
        for product_item in product_items:
            yield Request(product_item.url, callback=self.parse, meta={'product': product_item}, dont_filter=True)

    def parse(self,response):
        try:
            product_item = response.meta['product']
            data = json.loads(response.body)
            item = NikeItem()

            for section in data.get('sections', []):
                for product in section.get('products', []):
                    item['gender'] = product_item.gender
                    item['category'] = product_item.category
                    item['sub_category'] = product_item.sub_category
                    item['product_url'] = product.get('pdpUrl')
                    
                    yield Request(product.get('pdpUrl'), callback=self.parseNikeItem, meta={'item': item}, dont_filter=True)
            

            if data['nextPageDataService'] != None:
                next_page = data['nextPageDataService']
            yield scrapy.Request(next_page, callback=self.parse)
        except Exception, e:
            print str(e)

    def parseNikeItem(self, response):
        try:
            item = response.meta['item']
            item['product_url'] = response.request.url

            name = response.xpath("//*[contains(@class, 'exp-product-title')]/text()").extract()
            if len(name) == 0:
                name = response.xpath("//*[contains(@class, 'exp-pdp-title__main-title')]/text()").extract()

            item['name'] = ""
            if len(name) > 0:
                item['name'] = name[0].replace("\n", "").strip()

            item['price'] = ""
            price = response.xpath("//*[contains(@class, 'exp-pdp-local-price')]/text()").extract()
            if len(price) > 0:
                item['price'] = price[0].strip()

            item['code'] = ""
            code = response.xpath("//*[contains(@class, 'exp-style-color')]/text()").extract()
            if len(code) > 0:
                index = code[0].find("Style:")
                if index != -1:
                    item['code'] = code[0][index+6:].strip()

            item['image'] = ""
            imageURL = response.xpath("//*[contains(@class, 'exp-pdp-large-hero-image')]/@src").extract()
            if len(imageURL) == 0:
                imageURL = response.xpath("//*[contains(@class, 'js-imageGridImage')]/@src").extract()

            if len(imageURL) > 0:
                item['image'] = imageURL[0]

            yield item
        except Exception, e:
            print str(e)

    def getStyleCode(self, url):
        index = url.find("$img0=")
        start_code = url[index+6:]
        index = start_code.find("&")
        if index != -1:
            return start_code[:index]
        return start_code

class Item(object):
    def __init__(self, url, gender, category, sub_category):
        self.url = url
        self.gender = gender
        self.category = category
        self.sub_category = sub_category


