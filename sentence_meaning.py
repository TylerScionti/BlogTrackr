import nltk
from nltk import FreqDist, word_tokenize
from nltk.tree import Tree
import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup

def printChunks(chunk_name, tree):
    phrases = []
    print(chunk_name + " phrases: \n")
    for subtree in tree.subtrees(filter=lambda t: t.label() == chunk_name):
            if len(subtree.leaves()) > 1:
                phrases.append(" ".join([a for (a,b) in subtree.leaves()]))
    print (phrases)
    print("\n")
    return phrases

url = input("Enter a page URL:")
content = urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
content = soup.findAll('p')
stuff = str(content)

toks = nltk.tokenize.word_tokenize(stuff)

postoks = nltk.tag.pos_tag(toks)

grammar = r"""
    NNx2: {<NN.>+}
	NBAR: {<NN.*|JJ.>*<NN.*>}
    NBARx2: {<NBAR>(<IN><PRP.>?<DT>?<NBAR>)+}
    VRB: {(<NBAR>|PRP.)?<VB.><JBAR>?<IN>?<DT>?(<NBAR>|<JBAR>)}
        """
result= []
cp= nltk.RegexpParser(grammar)
tree = cp.parse(postoks)

nbarChunks = printChunks("NBAR", tree)
nbarx2Chunks = printChunks("NBARx2", tree)
pure_noun_phrases = printChunks("NNx2", tree)
printChunks("VRB", tree)
