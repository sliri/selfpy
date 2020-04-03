# 6.1.2
#################


def shift_left(my_list):
    """shift left"""
    out_list = [1, 2, 3]
    out_list[1] = my_list[0]
    out_list[2] = my_list[1]
    out_list[0] = my_list[2]
    return out_list
