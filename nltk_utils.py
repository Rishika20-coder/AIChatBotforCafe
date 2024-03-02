from gettext import install

import pip
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import nltk
nltk.download('punkt')
import numpy as np


def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words ):
    """sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog = [0, 1, 0, 1, 0, 0, 0]
    """

    # stem each word
    tokenized_sentence = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag

words = ["Organize","organizes","organizing"]
stemmed_words = [stem(w) for w in words]


sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = bag_of_words(sentence,words)


