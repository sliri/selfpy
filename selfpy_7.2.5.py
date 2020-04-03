# 7.2.5
#################


def delete_sequence(my_str):
    """ This function does something ot lists """
    returned_str = my_str[0]
    previous_char = my_str[0]
    for char in my_str:
        if char == previous_char:
            continue
        else:
            returned_str += char
            previous_char = char
    return returned_str


