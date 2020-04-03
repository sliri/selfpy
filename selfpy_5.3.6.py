# 5.3.6
#################


def fix_age(age):
    if 13 <= age <= 19:
        if (age == 15) or (age == 16):
            pass
        else:
            age = 0
    return age


#############################


def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c
