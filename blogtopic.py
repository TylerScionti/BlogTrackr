import nltk
from nltk import FreqDist, word_tokenize
from nltk.collocations import *
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

bigram_measures = nltk.collocations.BigramAssocMeasures()

print("Hello! Enter your blog's RSS feed and we'll tell you what it's about!")
url = input('Enter RSS feed here: ')
blog = feedparser.parse(url)
blog['feed']['title']

post = blog.entries[0]
content = post.content[0].value

soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

text = []

for word in stuff.split():
	if word.isalpha():
		text.append(word)


fdist1 = FreqDist(text)
words = sorted(w for w in set(text) if len(w) > 5 and fdist1[w] > 2)

print('Here are the topis we pulled out:')
for word in words:
	print('-' + word)


