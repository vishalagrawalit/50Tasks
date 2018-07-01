from nltk.corpus import wordnet

syn = wordnet.synsets("good")

# all synonyms
print(syn)

# first synonym
print(syn[0].name())

# just the word
print(syn[0].lemmas()[0].name())

# definition
print(syn[0].definition())

#example
print(syn[0].examples())

synonyms = []
antonyms = []

for s in syn:
    for l in s.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2))



