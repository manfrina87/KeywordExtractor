#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import nltk
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
from matplotlib import pyplot
 
from treetagger_python2 import *
from config_constants import *

# Split text into sentences
def sentence_splitter(text, lang=LANG):
    tokenizer = nltk.data.load('tokenizers/punkt/'+lang+'.pickle')
    sentences=tokenizer.tokenize(text.decode('utf-8'))
    for sentence in sentences:
        return treetagger(sentences)

# POS and lemma
def treetagger(sentence, lang=LANG):
    tt = TreeTagger(language=lang)
    pos_lemma=tt.tag(sentence)
    return pos_lemma

# create stop word list
def stopword(new_stops, lang=LANG):
    stops = list(set(stopwords.words(lang)))
    stops.extend(new_stops)
    return stops
        
# Filter words of documents
def cleaner(text, new_stops=NEW_STOPS, pos_filter=POS_FILTER):
    text=text.replace("'", " ")
    text=text.replace(",", " ")
    doc_clean=[]
    
    mystop=stopword(new_stops)
    
    for wd in sentence_splitter(text):
        regex = re.compile(pos_filter)  #POS filter
        if re.match(regex, wd[1]) is not None:
            if wd[2] != '<unknown>':            #lemmas instead of words
                doc_clean.append(wd[2])
            else:
                doc_clean.append(wd[0])
    
    filtered_words = [word.lower() for word in doc_clean if word not in mystop]   #stopwords filter + lowercase
    return filtered_words

#Remove Hapax
def hapax(tokens_nostop):
    freq_dist = nltk.FreqDist(tokens_nostop)
    rarewords = freq_dist.hapaxes()
    nohapax = [word for word in tokens_nostop if word not in rarewords]
    #print("Hapax Legomena removed... OK")
    return nohapax

#filter by freqlist
def freqlist(doc_clean):
    all_words = nltk.FreqDist(doc_clean)
    word_features = list(all_words.keys())[:FREQLIST_FILTER]    #freqlist filter
    return word_features

#Plot lexicon freqlist
def freqplot(words):
    freq_dist_nltk = nltk.FreqDist(words)
    freq_dist_nltk.plot(FREQLIST_PLOT_NUM, cumulative=True)
    pyplot.draw()
    pyplot.savefig(FREQLIST_PLOT_FILENAME)
    
