#!/usr/bin/env python2

#
#MODULES
#

import time
import re
import urllib3
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from matplotlib import pyplot

#
#METHODS
#

#Get page
def getpage(url):
    http = urllib3.PoolManager()
    r = http.request('GET',url)
    html = str(r.data)
    print("HTTP Request Status: " + str(r.status))
    return html

#Parse html
def parse(r):
    parse = BeautifulSoup(r, "html.parser")
    parse = parse.get_text()
    print("HTML parsed... OK")
    return parse
    
#Tokenize text
def tokenize(p):
    text = re.sub(r"\\.", " ",p)		#Remove control characters
    tokenizer = RegexpTokenizer('\w+')		#Delete punctuation
    toks = tokenizer.tokenize(text.lower())	#Lowercase and tokenize
    print("Text tokenized... OK")
    return toks

#Remove Stop Words
def stop(tokens):
    stoplist = stopwords.words('english')
    cleanwordlist = [tok for tok in tokens if tok not in stoplist]
    print("Stop Words removed... OK")
    return cleanwordlist

#Remove Hapax
def hapax(tokens_nostop):
    freq_dist = nltk.FreqDist(tokens_nostop)
    rarewords = freq_dist.hapaxes()
    nohapax = [word for word in tokens_nostop if word not in rarewords]
    print("Hapax Legomena removed... OK")
    return nohapax
    
#Plot Freq List
def freqlist(tokens_nohapax):
    freq_dist_nltk = nltk.FreqDist(tokens_nohapax)
    print(freq_dist_nltk)
    freq_dist_nltk.plot(50, cumulative=True)
    return freq_dist_nltk
    

#
#VARIABLES
#

url = 'https://ia800203.us.archive.org/15/items/ulysses04300gut/ulyss10h.htm'   #input param

r = getpage(url)

p = parse(r)

tokens = tokenize(p)

tokens_nostop = stop(tokens)

tokens_nohapax = hapax(tokens_nostop)

list = freqlist(tokens_nohapax) 

#list.plot(50, cumulative=False)	#Plot list freq with matplotlib


print('END')
