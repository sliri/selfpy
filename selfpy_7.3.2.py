# 7.3.2
#################


def check_win(secret_word, old_letters_guessed):
    """ This function does something ot chars """
    returned_list = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            returned_list[i] = secret_word[i] + ' '
        else:
            returned_list[i] = '_ '
    returned_str = ''.join(returned_list)

    string_no_spaces = returned_str.replace(" ", "")
    if string_no_spaces == secret_word:
        return True
    else:
        return False








