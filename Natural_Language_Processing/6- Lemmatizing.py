from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))
