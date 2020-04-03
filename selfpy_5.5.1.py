# 5.5.1
#################


def is_valid_input(letter_guessed):
    """ This function checks the  validity of the input letter """

    if letter_guessed.isalpha() and len(letter_guessed) == 1:
        return True
    else:
        return False
