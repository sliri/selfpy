# 7.2.1
#################


def is_greater(my_list, n):
    """ This function writes number bigger than n in list """
    bigger_than_list = []
    for num in my_list:
        if num > n:
            bigger_than_list.append(num)

    return bigger_than_list
