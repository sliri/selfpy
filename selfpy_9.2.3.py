# 9.2.3
#################


def who_is_missing(file_name):
    source_id = open(file_name, 'r')
    found_id = open(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/found.txt", 'w')
    source_str = source_id.read()
    source_list = (sorted(source_str.split(',')))
    sorted_list = list()
    for i in range(len(source_list)):
        sorted_list.append(int(source_list[i]))
    sorted_list.sort()
    for i in range(len(sorted_list)):
        if sorted_list[i + 1] - sorted_list[i] != 1:
            missing_num = sorted_list[i] + 1
            break
    found_id.write(str(missing_num))
    found_id.close()
    source_id.close()


def main():
    who_is_missing(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/numbers.txt")


if __name__ == "__main__":
    main()
