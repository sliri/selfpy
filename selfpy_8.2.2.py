# 8.2.2
#################


def myfun(s):
    return s[0][1]


def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=myfun, reverse=True)
