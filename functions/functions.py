import pandas as pd
import numpy as np


# select words of lenght 5
def by_size(words : list, size : int):
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
def rate_word(list_word:list,count_dict:dict):
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


# Keep Words with present letters 
def filter_present(dict_present:dict, initial_list:list) -> list:
    present_list = []
    if dict_present.__len__() == 0:
        present_list = initial_list.copy()
    else:
        for letter in dict_present.keys():
            if len(present_list) == 0:
                present_list = [word for word in initial_list if letter in word]
            else:
                cache = [i for i in initial_list if letter in i]
                present_list = [element for element in present_list if element in cache]
    
    return present_list

# Keep words with present letter wrong spot
def filter_present_spot(dict_present:dict,list_present:list) -> list:
    present_spot_list = list_present.copy()
    cache = []
    for letter in dict_present.keys():
        for postion in dict_present[letter]:
            print(letter, postion)
            for word in present_spot_list:
                if word.index(letter) == postion:
                    cache.append(word)
                        
    present_spot_out = [element for element in present_spot_list if element not in cache]

    return present_spot_out

# Remove words with absend letters 
def filter_absent(list_absent:list, initial_list:list) ->list:
    absent_list = []
    if len(list_absent) == 0:
        absent_list = initial_list.copy()
    else:
        for letter in list_absent:
            if len(absent_list) == 0:
                absent_list = [word for word in initial_list if letter not in word]
            else:
                cache = [word for word in initial_list if letter not in word]
                absent_list = [element for element in cache if element in absent_list]

    return absent_list

# Keep words with correct letters
def filter_correct(dict_correct:dict, list_present_spot:list) -> list:
    list_correct = list_present_spot.copy()
    cache = []
    for letter in dict_correct.keys():
        for word in list_correct:
            if dict_correct[letter] != word.index(letter):
                cache.append(word)

    list_correct_out = [element for element in list_correct if element not in cache]

    return list_correct_out