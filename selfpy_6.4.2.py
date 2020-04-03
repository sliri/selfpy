# 6.4.2
#################


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ This function checks the  validity of the input letter """
    if not(letter_guessed.isalpha()) or (len(letter_guessed) != 1) or (letter_guessed.lower() in old_letters_guessed):
        print('X')
        separator = '-> '
        arrow_st = separator.join(old_letters_guessed)
        print(arrow_st)
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True
