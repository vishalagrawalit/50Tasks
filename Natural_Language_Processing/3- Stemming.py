from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythonic", "pythoner", "pythoned"]

for w in example_words:
    print(ps.stem(w))
