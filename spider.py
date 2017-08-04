import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from blogtrackr_scraper.items import BlogtrackrScraperItem


"""
Uses this class from 'blogtrackr_scraper.items

import scrapy
from scrapy.item import Item, Field

class BlogtrackrScraperItem(scrapy.Item):
	url = Field() 

"""
class BlogTrackr(CrawlSpider):
	name = 'blogtrackr'
	allowed_domains = ['blogtrackr.com']
	start_urls = ['http://blogtrackr.com']

	rules = [
	Rule(LinkExtractor(allow=[r'.*']), callback='parse_item', follow=True)
	]
		
	def parse_item(self, response):
		href = BlogtrackrScraperItem()
		href['url'] = response.url
		return href
