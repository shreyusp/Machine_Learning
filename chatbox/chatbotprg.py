import nltk
import string
import numpy as np
import warnings
warnings.filterwarnings("ignore")

f=open("chatbot.txt","r")
raw=f.read()
sTokenizer=nltk.sent_tokenize(raw)
wTokenizer=nltk.word_tokenize(raw)

lemmer=nltk.stem.WordNetLemmatizer()

def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
removePunc=dict((ord(punct),None)for punct in string.punctuation)

def LemNormalizer(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(removePunc)))

userGreeting=("hello","hi","hey","Wasaaaaaap")
systemGreeting=["Hi","hey","HI there!","hello"]

import random

def greetCheck(sentence):
    for word in sentence.split():
        if word.lower() in userGreeting:
            return random.choice(systemGreeting)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def systemResponse(userText):
    sTokenizer.append(userText)
    tfidVect=TfidfVectorizer(tokenizer=LemNormalizer,stop_words='english')
    tfidMetrics=tfidVect.fit_transform(sTokenizer)
    similarity=cosine_similarity(tfidMetrics[-1],tfidMetrics)
    idx=similarity.argsort()[0][-2]
    sTokenizer.remove(userText)
    if(greetCheck(userText)!=None):
        response=greetCheck(userText)
    else:
        response=sTokenizer[idx]
    return response
    
        