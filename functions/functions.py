import pandas as pd
import numpy as np


# select words of lenght 5
def by_size(words, size):
    # l = filter(lambda x: len(x)==size, words)
    return [word for word in words if len(word) == size]


# create dictionary with counted letters
def count_letters(l):
    letter = dict() 
    letters = ["first","second","third","four","five"]
    for x in range(5):
        letter[letters[x]] = dict()
        for word in l:
            if (word[x] in letter[letters[x]].keys()) == False:
                letter[letters[x]][word[x]] = 1
            else:
                letter[letters[x]][word[x]] += 1
    return letter