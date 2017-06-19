import nltk
from nltk import FreqDist, word_tokenize
from nltk.tree import Tree
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

feed = feedparser.parse('http://m3wealthadvisors.com/blog/feed/')
for entry in feed['entries']:
	content = urlopen(entry['link']).read()
	soup = BeautifulSoup(content, "html.parser")
	content = soup.findAll('p')
	stuff = str(content)

toks = nltk.tokenize.word_tokenize(stuff)
postoks = nltk.tag.pos_tag(toks)

grammar = r"""
	NBAR: {<NN.*|JJ>*<NN.*>}  
    NP:
    	{<NN><NN>}
        {<NBAR>}
        {<NBAR><IN><NBAR>}"""
result= []
cp= nltk.RegexpParser(grammar)
tree = cp.parse(postoks)

phrases = []
for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
	if len(subtree.leaves()) > 1:
		phrases.append(subtree.leaves())

for phrase in phrases:
	my_ids = [idx for idx, val in phrase]
	print(" ".join(my_ids))
