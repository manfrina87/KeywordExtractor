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
from keyword_extractor import *

docs=[
    "Ancora allarme dopo la tensione di ieri con il test della bomba a idrogeno da parte della Corea del Nord. La Corea del Sud ha - infatti - registrato segnali relativi alla preparazione di un nuovo lancio di missile balistico.",
    "E'stato catturato in Uruguay il boss della 'ndrangheta Rocco Morabito, latitante da 25 anni. Morabito è stato preso in un hotel a Montevideo ma viveva nella località di Punta del Este.",
    ]
	
doc_clean=[]
for doc in docs:
    doc_clean.append(cleaner(doc))

print doc_clean
```
