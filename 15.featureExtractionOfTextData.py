# Feature Exteraction of text Data : Tf-idf Vectorizer 

'''
Feature Extraction = The mapping from textual data to real valued vectors(numbers) 

bag of words (BOW) = List of unique words in the text corpus(paragraph)

Term Frequency-Inverese Document Frequency(TF_IDF):
    To count the number of times each word appears in a document

Term Frequency(TF) = number of times term t appears in a document / Number of terms in the document

inverse document frequency (IDF) = log(N/n),where ,N is the number of words and n is the number 
                                    of documents a term t has appeared in

The IDF value of a rare word is high ,where as IDF of a frequent word is low.
'''
'''
fake news preadtion

about the dataset

1.id    : unique id for a news article 
2.title : the title of news article
3.author: author of the news article
4.text  : the text of the article , could be incomplete
5.label : a label that marks ,whether the news article is real or fake


1:fake
0:real
'''
# importing the dependancies

import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer

#  convert the textual data to feature vector 
# function loader

vectorizer=TfidfVectorizer()
vectorizer.fit('data')

X=vectorizer.transform("data") #this will tranfrom all the data into numric ,,and give the 
                               # corusponding tf-idf values store in X

"""
now we can feed this data into our model
"""