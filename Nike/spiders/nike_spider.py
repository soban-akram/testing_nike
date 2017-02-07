import scrapy
from scrapy.http import FormRequest
from scrapy.spiders import Spider 
from scrapy.selector import HtmlXPathSelector
from Nike.items import NikeItem
from scrapy.http import FormRequest, Request
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import json
start_url = 'http://store.nike.com/html-services/gridwallData?gridwallPath='
end_url = '&country=US&lang_locale=en_US'
class NikeCrawler(Spider):
    name = "nike"
    allowed_domains = ["store.nike.com"]
    def start_requests(self):
        main_url = [
            {'url': 'http://store.nike.com/html-services/gridwallData?gridwallPath=new-mens-tops-t-shirts/meZ7puZobp&country=US&lang_locale=en_US', 'gender': 'mens'}
        ]
        for main in main_url:
            yield Request(main['url'], callback=self.parseMainCategory, meta={'gender': main['gender']}, dont_filter=True)
        #product_items = [
            # ------------------------------------------- Mens ------------------------------------------------
            #Shoes
            # Item(start_url + 'new-mens-lifestyle-shoes/meZ7puZoneZoi3' + end_url, 'mens', 'shoes', 'lifestyle'),
            # Item(start_url + 'new-mens-running-shoes/meZ7puZ8yzZoi3' + end_url, 'mens', 'shoes', 'running'),
            # Item(start_url + 'new-mens-basketball-shoes/meZ7puZ8r1Zoi3' + end_url, 'mens', 'shoes', 'basketball'),
            # Item(start_url + 'new-mens-football-shoes/meZ7puZbgcZoi3' + end_url, 'mens', 'shoes', 'football'),
            # Item(start_url + 'new-mens-soccer-shoes/meZ7puZ896Zoi3' + end_url, 'mens', 'shoes', 'soccer'),
            # Item(start_url + 'new-mens-gym-training-shoes/meZ7puZ9hkZoi3' + end_url, 'mens', 'shoes', 'training & gym'),
            # Item(start_url + 'new-mens-skateboarding-shoes/meZ7puZ9yqZoi3' + end_url, 'mens', 'shoes', 'skateboarding'),
            # Item(start_url + 'new-mens-baseball-softball-shoes/meZ7puZbumZoi3' + end_url, 'mens', 'shoes', 'baseball/softball'),
            # Item(start_url + 'new-mens-golf-shoes/meZ7puZahaZoi3' + end_url, 'mens', 'shoes', 'golf'),
            # Item(start_url + 'new-mens-tennis-shoes/meZ7puZ8r0Zoi3' + end_url, 'mens', 'shoes', 'tennis'),
            # Item(start_url + 'new-mens-track-field-shoes/meZ7puZ9yoZoi3' + end_url, 'mens', 'shoes', 'track & field'),
            # Item(start_url + 'new-mens-lacrosse-shoes/meZ7puZaydZoi3' + end_url, 'mens', 'shoes', 'lacrosse'),
            #Compression & Nike Pro
            # Item(start_url + 'new-mens-nike-pro-compression-shirts/meZ7puZopr' + end_url, 'mens', 'compression & nike pro', 'tops'),
            # Item(start_url + 'new-mens-nike-pro-compression-bottoms/meZ7puZops' + end_url, 'mens', 'compression & nike pro', 'bottoms'),
            #Tops & T-Shirts
            # Item(start_url + 'new-mens-nike-pro-compression-shirts/meZ7puZona' + end_url, 'mens', 'tops & t-shirts', 'ompression & nike pro'),
            # Item(start_url + 'new-mens-long-sleeve-shirts/meZ7puZoeq' + end_url, 'mens', 'tops & t-shirts', 'long-sleeved'),
            # Item(start_url + 'new-mens-short-sleeve-shirts/meZ7puZoer' + end_url, 'mens', 'tops & t-shirts', 'short-sleeved'),
            # Item(start_url + 'new-mens-tank-tops-sleeveless-shirts/meZ7puZoel' + end_url, 'mens', 'tops & t-shirts', 'sleeveless & top tanks'),
            # Item(start_url + 'new-mens-polo-shirts/meZ7puZoem' + end_url, 'mens', 'tops & t-shirts', 'polos'),
            # Item(start_url + 'new-mens-jerseys/meZ7puZoeo' + end_url, 'mens', 'tops & t-shirts', 'jerseys'),
            # Item(start_url + 'new-mens-thermals-flannel-shirts/meZ7puZoen' + end_url, 'mens', 'tops & t-shirts', 'button-downs and flannels'),
            # Item(start_url + 'new-mens-graphic-t-shirts/meZ7puZrc5' + end_url, 'mens', 'tops & t-shirts', 'graphic t-shirts'),
            #Hoodies & Pullover
            # Item(start_url + 'new-mens-hoodies/meZ7puZoes' + end_url, 'mens', 'hoodies & pullover', 'hoodies'),
            # Item(start_url + 'new-mens-pullovers/meZ7puZoeu' + end_url, 'mens', 'hoodies & pullover', 'pullovers'),
            #Jaclets & Vests
            # Item(start_url + 'new-mens-jackets/meZ7puZoev' + end_url, 'mens', 'jaclets & vests', 'jackets'),
            # Item(start_url + 'new-mens-vests/meZ7puZoew' + end_url, 'mens', 'jaclets & vests', 'vests'),
            #Pants & Tights
            # Item(start_url + 'new-mens-joggers-sweatpants/meZ7puZpfo' + end_url, 'mens', 'pants & tights', 'joggers and sweatpants'),
            # Item(start_url + 'new-mens-nike-pro-compression-pants-tights/meZ7puZonb' + end_url, 'mens', 'pants & tights', 'compression & nike pro'),
            # Item(start_url + 'new-mens-pants/meZ7puZoex' + end_url, 'mens', 'pants & tights', 'pants'),
            # Item(start_url + 'new-mens-tights/meZ7puZoey' + end_url, 'mens', 'pants & tights', 'tights & leggings'),
            #Shorts
            # Item(start_url + 'new-mens-shorts/meZ7puZobt' + end_url, 'mens', 'shorts', ''),
            #Surf & Swimwear
            # Item(start_url + 'new-mens-boardshorts/meZ7puZnsv' + end_url, 'mens', 'surf & swimwear', 'boardshorts'),
            # Item(start_url + 'new-mens-compression/meZ7puZpfp' + end_url, 'mens', 'surf & swimwear', 'compression'),
            # Item(start_url + 'new-mens-rashguards-surf-shirts/meZ7puZnsz' + end_url, 'mens', 'surf & swimwear', 'rashguards & surf shirts'),
            # Item(start_url + 'new-mens-wetsuits/meZ7puZnsx' + end_url, 'mens', 'surf & swimwear', 'wetsuits'),
            #Socks
            # Item(start_url + 'new-mens-socks/meZ7puZpco' + end_url, 'mens', 'socks', ''),
            #Accessories & Equipment
            # Item(start_url + 'new-mens-bags-backpacks/meZ7puZof2' + end_url, 'mens', 'accessories & equipment', 'bags & backpacks'),
            # Item(start_url + 'new-mens-balls/meZ7puZof3' + end_url, 'mens', 'accessories & equipment', 'balls'),
            # Item(start_url + 'new-mens-belts/meZ7puZof5' + end_url, 'mens', 'accessories & equipment', 'belts'),
            # Item(start_url + 'new-mens-gloves/meZ7puZof7' + end_url, 'mens', 'accessories & equipment', 'gloves'),
            # Item(start_url + 'new-mens-hats-visors-headbands/meZ7puZof1' + end_url, 'mens', 'accessories & equipment', 'hats, visors & headbands'),
            # Item(start_url + 'new-mens-gear/meZ7puZofg' + end_url, 'mens', 'accessories & equipment', 'other'),
            # Item(start_url + 'new-mens-sleeves-arm-bands/meZ7puZofd' + end_url, 'mens', 'accessories & equipment', 'sleeves & arm bands'),
            # Item(start_url + 'new-mens-sunglasses/meZ7puZofe' + end_url, 'mens', 'accessories & equipment', 'sunglasses'),
            # Item(start_url + 'new-mens-training-gym-accessories/meZ7puZof6' + end_url, 'mens', 'accessories & equipment', 'training & gym'),
            # ------------------------------------------- Mens (END) ------------------------------------------------
            # ------------------------------------------- Womens ------------------------------------------------
            #Shoes
            # Item(start_url + 'new-womens-lifestyle-shoes/meZ7ptZoneZoi3' + end_url, 'womens', 'shoes', 'lifestyle'),
            # Item(start_url + 'new-womens-running-shoes/meZ7ptZ8yzZoi3' + end_url, 'womens', 'shoes', 'running'),
            # Item(start_url + 'new-womens-gym-training-shoes/meZ7ptZ9hkZoi3' + end_url, 'womens', 'shoes', 'training & gym'),
            # Item(start_url + 'new-womens-basketball-shoes/meZ7ptZ8r1Zoi3' + end_url, 'womens', 'shoes', 'basketball'),
            # Item(start_url + 'new-womens-soccer-shoes/meZ7ptZ896Zoi3' + end_url, 'womens', 'shoes', 'soccer'),
            # Item(start_url + 'new-womens-skateboarding-shoes/meZ7ptZ9yqZoi3' + end_url, 'womens', 'shoes', 'skateboarding'),
            # Item(start_url + 'new-womens-golf-shoes/meZ7ptZahaZoi3' + end_url, 'womens', 'shoes', 'golf'),
            # Item(start_url + 'new-womens-tennis-shoes/meZ7ptZ8r0Zoi3' + end_url, 'womens', 'shoes', 'tennis'),
            # Item(start_url + 'new-womens-track-field-shoes/meZ7ptZ9yoZoi3' + end_url, 'womens', 'shoes', 'track & field'),
            #Sports Bras
            # Item(start_url + 'new-womens-low-support-sports-bras/meZ7ptZoed' + end_url, 'womens', 'sports bras', 'low support'),
            # Item(start_url + 'new-womens-medium-support-sports-bras/meZ7ptZoee' + end_url, 'womens', 'sports bras', 'medium support'),
            # Item(start_url + 'new-womens-high-support-sports-bras/meZ7ptZoef' + end_url, 'womens', 'sports bras', 'high support'),
            #Compression & Nike Pro
            # Item(start_url + 'new-womens-nike-pro-compression-shirts/meZ7ptZopr' + end_url, 'womens', 'compression & nike pro', 'tops'),
            # Item(start_url + 'new-womens-nike-pro-compression-bottoms/meZ7ptZops' + end_url, 'womens', 'compression & nike pro', 'bottoms'),
            #Tops & T-Shirts
            #Item(start_url + '' + end_url, 'womens', 'tops & t-shirts', 'compression & nike pro'),
            #Hoodies & pullovers
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Jackets & Vests
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Pants & Rights
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Shorts
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Skirts & Dresses
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Surf & Swimwear
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Socks
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            #Accessories & Equipment
            #Item(start_url + '' + end_url, 'womens', 'shoes', 'lifestyle'),
            # ------------------------------------------- Womens (END) ------------------------------------------------
        #]
        # for product_item in product_items:
            # yield Request(product_item.url, callback=self.parse, meta={'product': product_item}, dont_filter=True)
    def parseMainCategory(self, response):
        try:
            gender = response.meta['gender']
            data = json.loads(response.body)
            dimensions = data.get('navigation').get('cartridges')[1].get('dimensions')
            categories = []
            for dim in dimensions:
                categories.append(Item(start_url + dim.get('slug') + '/' + dim.get('hash') + end_url, gender, dim.get('display'), '')) 
            for i, cat in enumerate(categories):
                yield Request(cat.url, callback=self.parseSubCategory, meta={'cat': cat, 'num': i}, dont_filter=True)

        except Exception, e:
            print str(e)
    def parseSubCategory(self, response):
        try:
            category = response.meta['cat']
            category_number = response.meta['num']
            data = json.loads(response.body)
            dimensions = data.get('navigation').get('cartridges')[1].get('dimensions')[category_number].get('dimensionValues')

            sub_categories = []
            if len(dimensions) == 0:
                sub_categories.append(category)
            else:
                for dim in dimensions:
                    sub_categories.append(Item(start_url + dim.get('slug') + '/' + dim.get('hash') + end_url, category.gender, category.category, dim.get('display'))) 

            for item in sub_categories:
                yield Request(item.url, callback=self.parse, meta={'product': item}, dont_filter=True)
        except Exception, e:
            print str(e)
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
