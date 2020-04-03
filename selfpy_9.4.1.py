# 9.4.1
#################


def choose_word(file_path, index):
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
    modulo_ind = (index-1) % len(file_data)
    chosen_word = file_data[modulo_ind]
    returned_tuple = (number_of_words, chosen_word)
    source_id.close()
    return returned_tuple


def main():
    index = 15
    l = choose_word(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/words.txt", index)
    print(l)


if __name__ == "__main__":
    main()
