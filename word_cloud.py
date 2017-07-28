from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.colors
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter a page URL:")
content = urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

colors=['#2F5EB6','#5E8DD9','#F4866A']

cmap = matplotlib.colors.ListedColormap(colors, name='simple', N=3)

wordcloud = WordCloud (max_font_size= 200,background_color="white", font_path = "/Library/Fonts/Arial Bold.ttf",
    width=1600, height=1000, prefer_horizontal=.6, relative_scaling=.4, colormap=cmap).generate(stuff)

plt.figure()
plt.imshow(wordcloud, interpolation='spline36')
plt.axis("off")
plt.show()
