import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("margot.txt")
sample_text = state_union.raw("gal_gadot.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_data)

tokenized = custom_sent_tokenizer(sample_text)

try:
    for w in tokenized:
        words = nltk.word_tokenize(w)
        tagged = nltk.pos_tag(words)
        print(tagged)
        
except Exception as e:
    print(str(e))
