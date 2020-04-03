# 9.1.2
#################


def op_file(file, op):
    if op == 'sort':
        returned_list = list()
        fileid = open(file)
        file_str = fileid.read().rstrip('\n').replace('\n', ' ').rsplit(' ')
        fileid.close()
        sorted_file_str = sorted(file_str)
        for word in sorted_file_str:
            if returned_list.count(word) >= 1:
                continue
            else:
                returned_list.append(word)
        print(returned_list)
        return returned_list

    elif op == 'rev':
        returned_line = list()
        fileid = open(file)
        for line in fileid:
            line_list = line.rstrip('\n').split(' ')
            reversed_line_list = (line_list[::-1])
            for word in reversed_line_list:
                returned_line.append(word[::-1])
                returned_str = (','.join(returned_line)).replace(',', ' ')
        print(returned_str)
        fileid.close()
        return returned_str

    elif op == 'last':
        user_num_lines = int(input("Please enter a number:"))
        fileid = open(file)
        i = 0
        for line in fileid:
            if i < user_num_lines:
                i += 1
            else:
                print(line.rstrip())
                i += 1




def main():
    op = 'last'
    op_file(r"/home/liron/PycharmProjects/untitled/hangman-ex1.4.2/textfile.txt", op)
    return None


if __name__ == "__main__":
    main()
