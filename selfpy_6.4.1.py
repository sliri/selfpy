# 6.4.1
#################


def check_valid_input(letter_guessed, old_letters_guessed):
    """ This function checks the  validity of the input letter """
    if not(letter_guessed.isalpha()) or (len(letter_guessed) != 1) or (letter_guessed in old_letters_guessed):
        return False
    else:
        return True
