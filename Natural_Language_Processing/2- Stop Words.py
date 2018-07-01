from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off the nltk's stopword."
stop_words = set(stopwords.words("english"))

# print(stop_words)
# List of nltk's pre defined stop words
'''
{'ll', 'was', 'more', 'for', 'a', 'of', "shouldn't", 'too', 'aren', 'with',
'some', "wouldn't", 'he', 'not', 'themselves', 'against', 'each', "she's",
'why', 'should', 'doesn', 'won', 'while', 'did', "needn't", 'your', 'yourselves',
'am', "weren't", 'how', 'this', 'my', 'just', 'is', 's', 'doing', "mustn't",
'them', 'isn', 'needn', 'between', 'y', 'most', 'it', "haven't", 'don', 'do',
'wouldn', 'being', "don't", 'yourself', "it's", 'o', 'or', 'him', 'yours',
'during', 'have', 'than', 'me', 'an', 'at', 'ourselves', 'through', 'weren',
'her', 'further', 'after', 'to', 'mightn', 'his', 'its', 'those', 'she',
"couldn't", 'you', 'hers', 'are', 'm', 'other', 'only', 'our', 'the',
'couldn', 'been', "aren't", 'that', "isn't", 't', 'has', 'off', 'above',
'didn', "mightn't", 'under', 'once', 'their', "hasn't", 'd', 'both', 'what',
'such', 'hadn', 'having', 'wasn', 'can', 'same', 'but', 'over', 'ain', 'by',
'if', 'again', 'into', 'will', 'there', 'here', 'when', "you've", 'and', 'out',
"doesn't", 'hasn', 'these', "hadn't", 'herself', "you're", 'on', 'be', 'myself',
'until', 'below', 'about', 'before', "that'll", 'theirs', 'had', 'from', 'so',
"should've", 'few', 'shouldn', 'they', 're', "you'll", 'mustn', 'himself', 'up',
"you'd", 'any', 'down', 'ma', 'in', 'where', "didn't", 'which', 'now', 'all', 'because',
'ours', 'shan', 'nor', 'very', "shan't", 'does', 'who', 've', 'were', 'whom', 'then',
'haven', 'i', 'no', 'as', 'itself', 'we', "wasn't", "won't", 'own'}
'''

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
