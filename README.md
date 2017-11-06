# Keyword extractor

A Python library to extract keywords from text ,filtering by POS tag and lemmatizing them.

## Install

### Install Treetagger + python-treetagger
1. Install [TreeTagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/);
2. Edit your ```~/.bashrc``` file, adding the ```treetagger/cmd``` path: 

```sh
nano ~/.bashrc 
export TREETAGGER_HOME='/path/to/your/TreeTagger/cmd/'
```

3. Install NLTK and its data:

```sh
sudo pip install nltk
sudo python -c "import nltk; nltk.download('punkt')"
sudo python -c "import nltk; nltk.download('stopwords')"
```
## Hello world
A simple use of the library

```py
from keyword_extractor import cleaner, hapax, freqlist, freqplot

List = open("MOTORI.txt").readlines()
doc_clean=[]

#Extract keywords
for doc in List:
    doc_clean.extend(cleaner(doc))

#Remove Hapax
myhapaxlist=hapax(doc_clean)
#Filter freqlist
myfreqlist=freqlist(myhapaxlist)


len(doc_clean)
len(myhapaxlist)
len(myfreqlist)
freqplot(doc_clean)
```
