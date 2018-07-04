import spacy
nlp=spacy.load('en')
doc = nlp(u'This is simple sentence')
for token in doc:
	print(token)
