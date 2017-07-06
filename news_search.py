import nltk
from nltk import FreqDist, word_tokenize
from urllib.request import urlopen
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import webhose

def news_search(keyword):
    webhose.config(token="97029546-2c7f-4116-a16d-e88dd66f09c2")
    r = webhose.search(keyword)
    for i in range(1):
        print(r.posts[i].title)

def getChunks(trees):
    chunks = {'NNx2': [], 'NBAR': [], 'NBARx2': []}
    for tree in trees:
        for subtree in tree.subtrees(filter=lambda t: t.label() in chunks):
            if len(subtree.leaves()) > 1:
                chunks[subtree.label()].append(" ".join([a for (a,b) in subtree.leaves()]))
    return chunks

url = input("Enter a page URL:")
content = urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

sents = nltk.sent_tokenize(stuff)

sent_lengths = []
for sent in sents:
    sent_lengths.append((len(sent)))

avg_sent_length = sum(sent_lengths) / len(sent_lengths)

grammar = r"""
    NNx2: {<NN.>+}
    NBAR: {<NN.*|JJ.>*<NN.*>}
    NBARx2: {<NBAR>(<IN><PRP.>?<DT>?<NBAR>)+}
    NandN: {<NBAR><CC><NBAR>}
    VRB: {(<NBAR>|PRP.)?<VB.><JBAR>?<IN>?<DT>?(<NBAR>|<JBAR>)}
        """
result= []
cp= nltk.RegexpParser(grammar)

trees = []
for sent in sents:
    long_sent = len(sent) > avg_sent_length
    if long_sent:
        sent_toks = nltk.word_tokenize(sent)
        stop_sym = ['/p', '>' ,'<' ,'p', '/a', 'img', 'alt=', '[']
        filtered = [ x for x in sent_toks if x not in stop_sym]
        postoks = nltk.tag.pos_tag(filtered)
        trees.append(cp.parse(postoks))


chunks = getChunks(trees)

terms = []

for key in chunks:
    print(key)
    for value in chunks[key]:
        if key =='NNx2':
            terms.append(value)
        else:
            print("-" + value + "\n")

print('*' * 50)

print(terms)

for keyword in terms:
    news_search(keyword)
