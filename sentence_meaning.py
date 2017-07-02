import nltk
from nltk import FreqDist, word_tokenize
from urllib.request import urlopen
from nltk.corpus import stopwords
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

sents = nltk.sent_tokenize(stuff)


print("Num words, and Num sentences:")
print(len(sents))
print("-" * 30)

print("Avg sentence length:")
sent_lengths = []
for sent in sents:
	sent_lengths.append((len(sent)))

avg_sent_length = sum(sent_lengths) / len(sent_lengths)
print(avg_sent_length)

print("-" * 30)
long_sents = []
print("Long Sentences:")
for sent in sents:
	long_sent = len(sent) > avg_sent_length
	if long_sent:
		print(sent)
		long_sents.append(sent)
long_sents = str(long_sents)

words = nltk.word_tokenize(long_sents)
stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in words if not w in stop_words]
postoks = nltk.tag.pos_tag(words)

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
