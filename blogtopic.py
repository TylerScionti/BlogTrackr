import nltk
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from nltk import FreqDist, word_tokenize
from nltk.collocations import *
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Prompt input with RSS feed URL and parse feed
url = input("Enter a RSS feed url: ")
feed = feedparser.parse(url)
for entry in feed['entries']:
	content = urlopen(entry['link']).read()
	soup = BeautifulSoup(content, "html.parser")
	content = soup.findAll('p')
	stuff = str(content)
#Create text blob string
blob = TextBlob(stuff)

text = []
#Tokenize text and remove stop words
for word in stuff.split():
	if word.isalpha():
		text.append(word)

stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in text if not w in stop_words]

#Find frequency of words, return words longer than 2 letters and used more than 3 times
fdist1 = FreqDist(clean_tokens)
words = sorted(w for w in set(clean_tokens) if len(w) > 2 and fdist1[w] > 3)

print('Here are the topis we pulled out:')
for word in words:
	print('-' + word, fdist1[word] )
#Pull all nowns
print('\n')
print('Nouns pulled:')
is_noun = lambda pos: pos[:2] == 'NN'
nouns = [word for (word, pos) in nltk.pos_tag(clean_tokens) if is_noun(pos)]
print(nouns)
#Pull text blob noun phrases
print('\n')
print('Nouns phrases:')
print(blob.noun_phrases)
