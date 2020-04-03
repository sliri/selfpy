# 7.2.2
#################


def numbers_letters_count(my_str):
    """ This function counts numbers and letters """
    digits = 0
    others = 0
    for char in my_str:
        if char.isdigit():
            digits += 1
        else:
            others += 1
    return[digits, others]
