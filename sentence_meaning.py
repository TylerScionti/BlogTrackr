import nltk
from nltk import FreqDist, word_tokenize
from nltk.collocations import *
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import conll2000
import matplotlib

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

grammar = r"""
	NBAR: {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns    
    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}"""
cp = nltk.RegexpParser(grammar, loop=2)
for sentence in sentences:
	result = cp.parse(sentence)
	print(result)
	result.draw()
