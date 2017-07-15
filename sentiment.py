import nltk
import random
from nltk import FreqDist, word_tokenize
from nltk.corpus import movie_reviews, stopwords
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import NuSVC
from nltk.classify import ClassifierI
from statistics import mode 

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers

	def classify(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)

	def confidence(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		
		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf

short_pos = open("pos.txt", "r").read()
short_neg = open("neg.txt", "r").read()

all_words = []
documents = []

allowed_word_types = ["J"]

for p in short_pos.split('\n'):
	documents.append( (p, "pos"))
	words = word_tokenize(p)
	pos = nltk.pos_tag(words)
	for w in pos:
		if w[1][0] in allowed_word_types:
			all_words.append(w[0].lower())

for p in short_neg.split('\n'):
	documents.append( (p, "neg"))
	words = word_tokenize(p)
	pos = nltk.pos_tag(words)
	for w in pos:
		if w[1][0] in allowed_word_types:
			all_words.append(w[0].lower())

save_documents = open("pickled_algos/documents.pickle", "wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

save_word_features = open("pickled_algos/word_features5k.pickle", "wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features


featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)
print(len(featuresets))

featuresets_f = open("pickled_algos/featuresets.pickle","wb")
pickle.dump(featuresets, featuresets_f)
featuresets_f.close()

training_set = featuresets[:10000]
testing_set = featuresets[10000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

save_classifier = open("pickled_algos/originalnaivebayes5k.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()


MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB Algo accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/mnbclassifier5k.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("Bernoulli Algo accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/bernoulliclassifier5k.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()


LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression Algo accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("pickled_algos/logisticregression5k.pickle", "wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()


NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC Algo accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

save_classifier = open("pickled_algos/nusvclassifier5k.pickle", "wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()


voted_classifier = VoteClassifier(classifier, 
				   MNB_classifier, 
				   BernoulliNB_classifier, 
				   LogisticRegression_classifier, 
				   NuSVC_classifier)
print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

def sentimen(text):
	feats = find_features(text)
	return voted_classifier.classify(feats)

