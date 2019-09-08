import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
import pickle

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_datasets(fname, t_type):
    data = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()
    return data
