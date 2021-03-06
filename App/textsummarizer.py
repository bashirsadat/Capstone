# -*- coding: utf-8 -*-
"""TextSummarizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLlp5I5JKWv8-jJJ0XXIM3O88os19w52
"""

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import nltk
import urllib.request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from string import punctuation
from heapq import nlargest
nltk.download('stopwords')
from collections import defaultdict
nltk.download('punkt')

url="https://en.wikipedia.org/wiki/Machine_learning"
request = urllib.request.urlopen(url).read().decode('utf8','ignore')

request

# read the data from the url
soup= BeautifulSoup(request, 'html.parser')
# find all text that has p tag
text_p = soup.find_all('p')
# print(text_p)



for i in range(0,len(text_p)):
    text += text_p[i].text
text = text.lower()
# tokenize the text
tokens =[t for t in text.split()]
# print(tokens)

clean_token =tokens[:]
#define irrelevant words that include stop words , punctuations and numbers
stopword = set(stopwords.words('english') + list(punctuation) + list("0123456789") )
for token in tokens:
    if token in stopword:
        clean_token.remove(token)

# print(clean_token)

freq = nltk.FreqDist(clean_token)
top_words=[]
top_words=freq.most_common(100)
# print(top_words)

sentences = sent_tokenize(text)
# print(sentences)

ranking = defaultdict(int)
for i, sent in enumerate(sentences):
    for word in word_tokenize(sent.lower()):
        if word in freq:
            ranking[i]+=freq[word]
    top_sentences = nlargest(10, ranking, ranking.get)
# print(top_sentences)

# print(sentences[2])

sorted_sentences = [sentences[j] for j in sorted(top_sentences)]
print(sorted_sentences)
if __name__ == '__main__':
    main()