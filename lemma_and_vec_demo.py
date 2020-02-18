"""

This script demonstrates the lemmatization of a few words 
as well a small demo comparing the similarities between words using word vectors

"""


from nltk import word_tokenize, pos_tag, WordNetLemmatizer, download
from nltk.corpus import wordnet, stopwords
import time

lemmatizer = WordNetLemmatizer() 

def print_lemma(w):
    """
    This file uses the WordNet system to lemmatize the words, which essentially brings most words to a simpler form
    The part of speech is useful in converting a word to its lemma,
    However, since a single word is used without its sentence, the library can't predict the part of speech,
    So the fact that all demo words are verbs are used only for this demo
    """
    for w, pos in pos_tag([w]):
        print(w + ": " + lemmatizer.lemmatize(w, pos="v"))

print("lemmatization demo: ")
print_lemma("cook")
print_lemma("cooks")
print_lemma("cooking")
print_lemma("cooked")

print()

import gensim.downloader as api
# from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import numpy as np
from scipy.spatial.distance import cosine

# print("downloading")
# corpus = api.load('text8')
# model = Word2Vec(corpus)

print("loading")
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
# Loading Google's pretrained system that has more than 3 billion words installed

print()

def print_vec_distance(w1, w2):
    t0 = time.time()
    sim = model.similarity(w1, w2)
    print(f"{w1} / {w2}: {str(sim)}")
    print("comparison time: " + str( time.time() - t0))
    print()



# This is to demonstrate the similarity between the vectors for each word (compared to a negative control). 
# Due to their similarity, we may be able to get away with not lemmatizing or stemming for a slight boost to speed

print("Word Vector Distances:") 
print_vec_distance("cook", "cooks")
print_vec_distance("cooked", "cooking")
print_vec_distance("cook", "manslaughter")

print()

print_vec_distance("entrepreneur", "entrepreneurial")
print_vec_distance("entrepreneurial", "entrepreneurship")
print_vec_distance("entrepreneur", "salt")
