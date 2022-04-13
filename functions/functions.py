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


def word_list_adjust(privious_list, dict_correct_wrong, list_worng, dict_correct):
    filter_correct = []
    # keep words which contain the correct letters
    for letter in dict_correct_wrong.keys():
        if len(filter_correct) == 0:
            filter_correct = [word for word in privious_list if letter in word]
        else:
            cache = [i for i in privious_list if letter in i]
            filter_correct = [element for element in filter_correct if element in cache]

    # delete words from list containing worng letters
    word_list = []
    for l in range(len(list_worng)):
        if len(word_list) == 0:
            word_list = [i for i in filter_correct if list_worng[l] not in i]
        else:
            cache = [i for i in filter_correct if list_worng[l] not in i]
            word_list = [element for element in word_list if element in cache]

    # removing words with check letters in worng spot
    proof = len(word_list)-1
    while len(word_list) != proof:
        print(len(word_list))
        proof = len(word_list)
        for letter in dict_correct_wrong.keys():
            # print(letter)
            for postion in dict_correct_wrong[letter]:
                print(postion)
                for word in word_list:
                    # if word == "isbas":
                    #     print("Fuck",postion, word.index(letter))
                    # if dict_correct_wrong[letter][postion] == word.index(letter):
                    #     word_list.remove(word)
                    if postion == word.index(letter):
                        word_list.remove(word)
    fucking_list = word_list.copy()
    for letter in dict_correct.keys():
        print(letter)
        # print(letter)
        print(fucking_list)
        print("\n")
        for word in fucking_list:
            print(word)
            if word == "isbas":
                print("Fuck",dict_correct[letter], word.index(letter))
            if dict_correct[letter] != word.index(letter):
                fucking_list.remove(word)

    
    return fucking_list 

