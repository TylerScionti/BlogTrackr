import nltk
from nltk import FreqDist, word_tokenize
from nltk.collocations import *
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

bigram_measures = nltk.collocations.BigramAssocMeasures()

print("Hello! Enter your blog's RSS feed and we'll tell you what it's about!")
url = input('Enter RSS feed here: ')

#parses the blog feed URL
blog = feedparser.parse(url)
blog['feed']['title']
#selects the first blog post from the feed
post = blog.entries[0]
content = post.content[0].value
#strips the feed of extra markup, retains the raw text
soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

text = []
#breaks the text into individual words in a list 'text'
for word in stuff.split():
	if word.isalpha():
		text.append(word)

#finds words longer than 5 letters and used more than 2 times
fdist1 = FreqDist(text)
words = sorted(w for w in set(text) if len(w) > 5 and fdist1[w] > 2)
#prints the words to the screen
print('Here are the topis we pulled out:')
for word in words:
	print('-' + word)


