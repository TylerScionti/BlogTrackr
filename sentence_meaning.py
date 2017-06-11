import nltk
from nltk import FreqDist, word_tokenize
from nltk.collocations import *
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

sentences = nltk.sent_tokenize(stuff)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]

print(sentences)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
for sentence in sentences:
	result = cp.parse(sentence)
print(result)
