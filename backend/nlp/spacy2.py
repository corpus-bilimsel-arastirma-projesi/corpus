# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:48:15 2019

@author: asuer
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 20 08:49:46 2019

@author: asuer
"""

import json
import time
import re
import spacy
import gensim
import pickle
import matplotlib.pyplot as plt
import pyLDAvis.gensim

import os, re, operator, warnings

warnings.filterwarnings('ignore')  # Let's not pay heed to them right now

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation

with open("/home/abraham/PycharmProjects/corpus-backend/media/UK_afterJaccard_SeDMiZa.json") as datafile:
    data = json.load(datafile)

do = data["content"]
# import itertools
# do=dict(itertools.islice(do.items(), 2))

start = time.time()
nlp = spacy.load("en_core_web_sm")  # , disable = ['parser', 'textcat'])
my_stop_words = [u'say', u'\'s', u'mr', u'be', u'said', u'says', u'saying', 'today', '\n ', '\n']
for stopword in my_stop_words:
    lexeme = nlp.vocab[stopword]
    lexeme.is_stop = True
texts = []
for document in do:
    do[document] = re.sub(r'[^\x00-\x7f]', r'', do[document])
    doc = nlp(do[document])
    texts.append(doc)
end = time.time()
print(end - start)

###### from here ######
# with open("D:/Google Drive/BAP/text_analysis/mycorpus.txt", "wb") as fp:   #Pickling
# pickle.dump(texts, fp)

with open("D:/Google Drive/BAP/text_analysis/mycorpus.txt", "rb") as fp:  # Unpickling
    texts = pickle.load(fp)

from collections import Counter

# POS: w.pos_ ' w.dep_ , w.head.text
# NER:  w.ent_type_
#
start = time.time()
txts = []
for i in texts:
    ion = []
    for w in i:
        if not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
            ion.append((w.text, w.ent_type_))
    txts.append(ion)
end = time.time()
print(end - start)
Counter(txts[0]).most_common(20)

txts = []
for i in texts:
    ion = []
    for chunk in i.noun_chunks:
        ion.append((chunk.text, chunk.root.text, chunk.root.dep_,
                    chunk.root.head.text))
    txts.append(ion)
Counter(txts[0]).most_common(20)

txts = []
for i in texts:
    ion = []
    for w in i:
        if not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
            ion.append((w.text, w.dep_, w.head.text, w.head.pos_,
                        [child for child in w.children]))
    txts.append(ion)

from spacy.symbols import nsubj, VERB

txts = []
for i in texts:
    verbs = set()
    for possible_subject in i:
        if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
            verbs.add(possible_subject.head)
    txts.append(verbs)

# find phrases using the syntactic head.
root = [token for token in texts[1] if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
          descendant.n_rights, [ancestor.text for ancestor in
                                descendant.ancestors])

adjectives = []
for sent in texts[1].sents:
    for word in sent:
        if 'intelligence' in word.string:
            for child in word.children:
                if child.pos_ == 'ADJ':
                    adjectives.append(child.string.strip())

Counter(adjectives).most_common(10)

#####GENSIM##########
from gensim.corpora import Dictionary

# gensim parameters:
# chunksize:  controls how many documents are processed . Increasing it will speed up training,
# passes: This controls how often we train the model on the entire corpus.
# iterations: This controls how often we repeat a particular loop over each document.

####
txts = []
for i in texts:
    ion = []
    for w in i:
        if not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
            ion.append((w.lemma_))
    txts.append(ion)
bigram = gensim.models.Phrases(txts)
txts = [bigram[line] for line in txts]
dictionary = Dictionary(txts)
# dictionary.filter_extremes(no_below=20, no_above=0.5)
corpus = [dictionary.doc2bow(text) for text in txts]

Counter(txts[1]).most_common(20)

len(dictionary)

dictionary.filter_n_most_frequent(2)
len(dictionary)

gensim.corpora.MmCorpus.serialize("D:/Google Drive/BAP/text_analysis/corpus.mm", corpus)  ###SAVE

corpus = gensim.corpora.MmCorpus("D:/Google Drive/BAP/text_analysis/corpus.mm")  ###LOAD
print(list(corpus))  # calling list() will convert any sequence to a plain Python list

print(corpus)
for doc in corpus:
    print(doc)

from gensim.models import LdaModel, LsiModel, HdpModel

# tf=idf traNnsformation
from gensim import models

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

######
# Alpha: the document-topic density. Higher:  documents are composed of more topics
# Beta:  topic-word density. higHER: topics are composed of a large number of words

ldamodel = gensim.models.LdaModel(corpus=corpus_tfidf, num_topics=25, id2word=dictionary)
ldamodel.show_topics()
ldamodel.show_topics()[1]
# document-topic proportions
ldamodel[corpus_tfidf[0]]

ldamodel.get_term_topics("oberlander")

lsimodel = gensim.models.LsiModel(corpus=corpus, num_topics=10, id2word=dictionary)
lsimodel.show_topics(num_topics=10)  # Showing only the top 5 topics

from gensim.models import HdpModel

hdpmodel = gensim.models.HdpModel(corpus=corpus, id2word=dictionary)
hdpmodel.show_topics()  # Showing only the top 5 topics

######NMF####


# for document in tfidf[corpus]:
# print(document)


import numpy as np

corpus_tfidf = np.array(corpus_tfidf)
all_topics_csr = gensim.matutils.corpus2csc(corpus)
corpus_tfidf = all_topics_csr.T.toarray()

from sklearn.decomposition import NMF, LatentDirichletAllocation

no_topic = 10

model = NMF(n_components=2, init='random', random_state=0)
nmf = model.fit_transform(corpus_tfidf)

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF


# buradan sonarsi beceremedim
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ").join([feature_names[i]
                         for i in topic.argsort()[:-no_top_words - 1:-1]])


no_top_words = 10

display_topics(nmf, no_top_words)


def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print
        "Topic %d:" % (topic_idx)
        print
        " ".join([feature_names[i]
                  for i in topic.argsort()[:-no_top_words - 1:-1]])


no_features = 1000

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(skl_texts)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(skl_texts)
tf_feature_names = tf_vectorizer.get_feature_names()

no_topics = 10

# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,
                                random_state=0).fit(tf)

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)
