#A RSS reader, you enter the RSS feed URL and the content is parsed and printed

import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter a RSS feed url: ")

feed = feedparser.parse(url)

for entry in feed['entries']:
	content = urlopen(entry['link']).read()
	soup = BeautifulSoup(content, "html.parser")
	content = soup.findAll('p')
	stuff = str(content)
	print(stuff)
