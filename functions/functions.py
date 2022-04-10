import pandas as pd
import numpy as np


# select words of lenght 5
def by_size(words, size):
    size_list = [word for word in words if len(word) == size]
    alpha_list = [i for i in size_list if i.isalpha()] 
    return alpha_list


# create dictionary with counted letters
def count_letters(l):
    letter = dict() 
    letters = range(5)
    for x in range(5):
        letter[letters[x]] = dict()
        for word in l:
            if (word[x] in letter[letters[x]].keys()) == False:
                letter[letters[x]][word[x]] = 1
            else:
                letter[letters[x]][word[x]] += 1
    return letter