"""Named Entity Recognition"""
import spacy
from urllib import request
def cleanup(token, lower = True):
	if lower:
		token = token.lower()
	return token.strip()
url = 'https://cdncontribute.geeksforgeeks.org/wp-content/uploads/e-mail-1.txt'
response = request.urlopen(url)
raw = response.read().decode('utf8')
nlp = spacy.load('en')
document=nlp(raw)
labels = set([w.label_ for w in document.ents])
for label in labels: 
    entities = [cleanup(e.string, lower=False) for e in document.ents if label==e.label_] 
    entities = list(set(entities)) 
    print (label,entities)