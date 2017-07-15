import sentiment_mod as s
import nltk
from nltk import FreqDist, word_tokenize
from urllib.request import urlopen
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

post = input("Enter a blog post URL: ")
content = urlopen(post).read()
soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

print(s.sentiment(stuff))

