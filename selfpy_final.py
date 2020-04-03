def print_start_screen():
    print("""\
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ 
                         """)


def choose_word(file_path):
    # file_path = str(input("Enter file path:"))
    index = int(input("Enter_index:"))
    source_id = open(file_path, 'r')
    file_data = source_id.read().replace('\n', ' ').split(' ')
    sorted_file_data = sorted(file_data)
    words_bank = list()
    for word in sorted_file_data:
        if word not in words_bank:
            words_bank.append(word)
        else:
            continue

    number_of_words = len(words_bank)
    modulo_ind = (index - 1) % len(file_data)
    chosen_word = file_data[modulo_ind]
    returned_tuple = (number_of_words, chosen_word)
    source_id.close()
    return returned_tuple[1]


def show_lines(word):
    print('Let\'s Start!')
    print_hangman(0)
    print('_ ' * (len(word)))


def print_hangman(num_of_tries):
    """
    VARIABLE-  HANGMAN_PHOTOS (dict)- from unit 1
    the FUNCTION PRINT:
    one of the 7 photos in HANGMAN_PHOTOS-
    with the help of a VARIABLE-num_of_tries that represent
    how many times the user
    guessed the wrong letter, and  HANGMAN_PHOTOS
    dict[key] = value
    """
    # images for the wrong gusses

    # picture 1:
    image1 = "x-------x"
    # picture 2:
    image2 = """x-------x
|
|
|
|
|"""
    # picture 3:
    image3 = """x-------x
|       |
|       0
|
|
|"""
    # picture 4:
    image4 = """x-------x
|       |
|       0
|       |
|
|"""
    # picture 5:
    image5 = """x-------x
|       |
|       0
|      /|\\
|
|"""
    # picture 6:
    image6 = """x-------x
|       |
|       0
|      /|\\
|      /
|"""
    # picture 7:
    image7 = """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""

    HANGMAN_PHOTOS = {0: image1, 1: image2, 2: image3, 3: image3, 4: image4, 5: image5, 6: image6, 7: image7}

    print(HANGMAN_PHOTOS[num_of_tries])


def get_letter():
    current_guess = input("Guess a letter:")
    return current_guess


def old_letters_guess_bank(letter, old_letters_guessed):
    if letter not in old_letters_guessed:
        old_letters_guessed.append(letter)
    return old_letters_guessed


def check_valid_input(letter_guessed, old_letters_guessed):
    """ This function checks the  validity of the input letter """
    if not (letter_guessed.isalpha()) or (len(letter_guessed) != 1) or (letter_guessed in old_letters_guessed):
        return False
    else:
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """ This function does something ot chars """
    returned_list = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            returned_list[i] = secret_word[i] + ' '
        else:
            returned_list[i] = '_ '
    returned_str = ''.join(returned_list)
    return returned_str


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


def main():
    print_start_screen()
    secret_word = choose_word(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/words.txt")
    show_lines(secret_word)

    num_of_trials = 0
    MAX_TRIALS = 6
    old_letters_guessed = list()
    while num_of_trials < MAX_TRIALS:
        current_guess = get_letter()
        valid_guess = check_valid_input(current_guess, old_letters_guessed)
        if valid_guess:
            old_letters_guessed = old_letters_guess_bank(current_guess, old_letters_guessed)
            if current_guess in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed):
                    print('WIN :)')
                    return
            else:
                print(':(')
                num_of_trials += 1
                print_hangman(num_of_trials)
                print(show_hidden_word(secret_word, old_letters_guessed))
        else:
            print('X')
    print('LOOSE :(')
    return


if __name__ == "__main__":
    main()
