from os import path
import nltk
import ssl
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.colors
from urllib.request import urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

posts = open("out.csv","r").read()
lines = posts.split('\n')

stuff = ""

for post in lines:
    try:
        content = urlopen(post, context=ctx).read()
        soup = BeautifulSoup(content, "html.parser")
        content = soup.findAll('p')
        stop_sym = ['/p', '>' ,'<' ,'p', '/a', 'img', 'alt=', '[', 'span', 'p1', 'href', 'Mailchimp', 'wpcf7 form', 'src', 'https', 'http', 'readmore']
        filtered = [ x for x in content if x not in stop_sym]
        stuff += str(filtered)
    except ValueError:
        pass

def on_error(self, status):
	print(status)

colors=['#2F5EB6','#5E8DD9','#F4866A']

cmap = matplotlib.colors.ListedColormap(colors, name='simple', N=3)

wordcloud = WordCloud (max_font_size= 200,background_color="white", font_path = "/Library/Fonts/Arial Bold.ttf",
    width=1600, height=1000, prefer_horizontal=.6, relative_scaling=.4, colormap=cmap).generate(stuff)

plt.figure()
plt.imshow(wordcloud, interpolation='spline36')
plt.axis("off")
plt.show()
