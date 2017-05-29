import scrapy
from scrapy.selector import HtmlXPathSelector
from blogtrackr_sample.items import BlogTrackrSampleItem


class QuotesSpider(scrapy.Spider):
    name = "blogtrackr"
    start_urls = [
        'http://blogtrackr.com/blog',
    ]

    def parse(self, response):
        for title in response.css('h1'):
        	yield {
        	'text': title.css('h1').extract()
        	}
