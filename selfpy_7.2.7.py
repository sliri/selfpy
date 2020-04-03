# 7.2.7
#################


def arrow(my_char, max_length):
    """ This function does something ot chars """
    for i in range(1, max_length * 2):
        if i <= max_length:
            print(my_char * i)
        else:
            print(my_char * (max_length * 2 - i))


