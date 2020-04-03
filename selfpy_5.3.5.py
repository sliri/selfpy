# 5.3.5
#################


def distance(num1, num2, num3):
    condition1 = abs(num2 - num1) < 1
    condition2 = abs(num3 - num1) < 1
    condition3 = abs(num2 - num1) > 2 and abs(num2 - num3) > 2
    condition4 = abs(num3 - num1) > 2 and abs(num3 - num2) > 2

    if (condition1 and not condition2) or (condition2 and not condition1) and \
            (condition3 and not condition4) or (condition4 and not condition3):
        return True
    else:
        return False
