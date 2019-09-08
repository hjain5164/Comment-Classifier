from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.stem import WordNetLemmatizer
import numpy as np

#for regurlar expressions
import re

#for configuration
import config

def toxicity_score(comment):
	'''
	check comment for toxicity
	input: string
	output: value between 0 - 1 indicating toxicity
	'''
	num_toxic_words = 0

	words = comment.split(' ')
	print("Words:", words)

	for word in words:

		# keep only alphabet characters!
		word = re.sub('[^a-zA-Z]+', '', word)
		# convert to lowercase
		word = word.lower()
		if word in config.toxic_words:
			num_toxic_words += 1

	print(f"Toxic Words found:{num_toxic_words}")
	print(f"Comment Length:{len(words)}")
	score = num_toxic_words / len(words)
	return score

def stemSentence(comment):
    #for word tokenisation
    token_words=word_tokenize(comment)
    token_words
    stem_sentence=[]

    for word in token_words:
        #porterstem word stemming method is used
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
        
    return "".join(stem_sentence)

def lem(comment):
    wordnet_lemmatizer = WordNetLemmatizer()
    #for removing the punctuatuins from the code
    punctuations="?:!.,;"
    sentence_words = nltk.word_tokenize(comment)
    
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)
            
    return sentence_words
    

