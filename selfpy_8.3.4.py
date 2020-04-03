# 8.3.4
#################
import datetime
from datetime import date


def inverse_dict(my_dict):
    inverse_dictionary = {}
    for key in my_dict:
        val = my_dict[key]  # which is the value!
        print(val)
        inverse_dictionary.setdefault(val, []).append(key)  # appending to list
    return inverse_dictionary

