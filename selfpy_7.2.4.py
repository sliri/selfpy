# 7.2.4
#################


def seven_boom(end_number):
    """ This function plays 7 boom """
    returned_list = []
    for i in range(end_number+1):
        if i % 7 == 0 or '7' in str(i):
            returned_list.append('BOOM')
        else:
            returned_list.append(i)
    return returned_list
