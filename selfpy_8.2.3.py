# 8.2.3
#################


def mult_tuple(tuple1, tuple2):
    returned_list = list()
    for number1 in tuple1:
        for number2 in tuple2:
            returned_list.append((number1, number2))
            returned_list.append((number2, number1))
    return tuple(returned_list)
