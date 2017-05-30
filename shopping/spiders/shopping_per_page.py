from scrapy.spiders import Spider
from shopping.items import ShoppingItem
from scrapy.http    import Request
 
class MySpider(Spider):
	name = "shopping_per_page"
	allowed_domains = ["www.shopping.com"]
	
	def __init__(self, page=1, key='bag', *args, **kwargs):
		super(MySpider, self).__init__(*args, **kwargs)
		self.start_urls = ["http://www.shopping.com/products~PG-" + page + "?KW=" + key]
		

	def parse(self, response):
		products = response.xpath('//div[contains(@class, "gridItemBtm")]')
		items = []
		for product in products:
			item = ShoppingItem()
			productName = product.xpath('h2/a/span/@title').extract()
			price = product.xpath('div/span/a/text()').extract()
			company = product.xpath('div/a/text()').extract()
			try:
				item['productName'] = productName[0].strip('\n')
			except IndexError:
				item['productName'] = productName
			try:
				item["price"] = price[0].strip('\n')
			except IndexError:
				item["price"] = price
			try:
				item["company"] = company[0].strip('\n')
			except IndexError:
				item["company"] = company
			yield item


class ShoppingSpider(Spider):
	name = "shopping"
	allowed_domains = ["www.shopping.com"]
	
	def __init__(self, key='bag', *args, **kwargs):
		super(ShoppingSpider, self).__init__(*args, **kwargs)
		self.start_urls = ["http://www.shopping.com/products?KW=" + key]
		

	def parse(self, response):
		products = response.xpath('//div[contains(@class, "gridItemBtm")]')
		items = []
		for product in products:
			item = ShoppingItem()
			productName = product.xpath('h2/a/span/@title').extract()
			price = product.xpath('div/span/a/text()').extract()
			company = product.xpath('div/a/text()').extract()
			try:
				item['productName'] = productName[0].strip('\n')
			except IndexError:
				item['productName'] = productName
			try:
				item["price"] = price[0].strip('\n')
			except IndexError:
				item["price"] = price
			try:
				item["company"] = company[0].strip('\n')
			except IndexError:
				item["company"] = company
			yield item

