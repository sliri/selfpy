# 8.3.3
#################
import datetime
from datetime import date


def count_chars(my_str):
    my_dict = {}
    for letter in my_str:
        if not(letter in my_dict) and (letter != ' '):
            my_dict[letter] = my_str.count(letter)
    return my_dict
