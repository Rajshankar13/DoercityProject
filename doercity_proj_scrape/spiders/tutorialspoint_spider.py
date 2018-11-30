import scrapy

class tutorialspointSpider(scrapy.Spider):
	name = "tutorialspoint_Spider"

	def start_requests(self):
		url = 'https://www.tutorialspoint.com/dbms/index.htm'
		yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		p_selectors = response.selector.xpath("//div[starts-with(@class, 'col-md-7')]/p")
		for selector in p_selectors:
			yield {
				'page': response.url,
				'content': selector.xpath("text()").extract_first()
			}

		next_page = response.selector.xpath("//div[@class='nxt-btn']/a/@href").extract_first()
		if next_page is not None:
			next_page_link = response.urljoin(next_page)
			yield scrapy.Request(url = next_page_link, callback = self.parse)	