"""Part Of Speech Tagging"""
import spacy
from urllib import request
url = 'https://cdncontribute.geeksforgeeks.org/wp-content/uploads/e-mail-1.txt'
response = request.urlopen(url)
raw = response.read().decode('utf8')
nlp=spacy.load('en')
doc = nlp(raw)
tag_list=[{word.pos:word.pos_} for word in doc]
print(tag_list)

#OutPut
# [{90: 'INTJ'}, {102: 'SPACE'}, {89: 'DET'}, {99: 'VERB'}, {95: 'PROPN'}, {102: 'SPACE'}, {95: 'PROPN'}, {102: 'SPACE'}, {95: 'PROPN'}, {102: 'SPACE'}, {95: 'PROPN'}, {99: 'VERB'}, {89: 'DET'}, {91: 'NOUN'}, {84: 'ADP'}, {91: 'NOUN'}, {102: 'SPACE'}, {95: 'PROPN'}, {102: 'SPACE'}, {95: 'PROPN'}]

#Processing First Sentence
document=nlp(raw)
for word in list(document.sents)[0]:
	print(word,word.tag_)