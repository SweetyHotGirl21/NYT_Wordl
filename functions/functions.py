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

# Assigned values of letters to words from list
def rate_word(list_word,count_dict):
    output_long = dict()
    output_short = dict()
    for word in list_word:
        output_long[word] = dict()
        output_long[word]["count"] = 0
        output_short[word] = 0
        for key in count_dict:
            if  word[key] in output_long[word].keys():
                output_long[word]["count"] += 0
                output_short[word] += 0
            else:
                output_long[word][word[key]] = count_dict[key][word[key]]
                output_long[word]["count"] += count_dict[key][word[key]] 
                output_short[word] += count_dict[key][word[key]]
    return output_long, output_short
