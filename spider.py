import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from blogtrackr_sample.items import BlogTrackrSampleItem


class QuotesSpider(CrawlSpider):

	name = "blogtrackr"
	allowed_domains = ["blogtrackr.com"]
	start_urls = [
	'http://blogtrackr.com/blog']
	rules = [Rule(LinkExtractor(allow=[r'.*']), follow=True),
            Rule(LinkExtractor(allow=[r'@href']), callback='parse_links')]
	
	def parse_links(self, response):
		filename = "test.txt"
		archive = open(filename, 'wb')
		extractor = LinkExtractor(allow=r'blog\d+')
		for link in extractor.extract_links(response):
			url = link.urlextractor = LinkExtractor(allow=r'blog\d+')
			achrive.writelines("%s\n" % url)                
			print(url)
