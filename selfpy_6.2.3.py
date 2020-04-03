# 6.2.3
#################


def format_list(my_list):
    """doing some stuff on list"""
    separator = ', '
    returned_str = separator.join(my_list[::2])+', '+'and ' + my_list[-1]
    return returned_str
