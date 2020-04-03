# 2.3.3
#################
EnteredNum = int(input(" Enter three digits (each digit for one pig):"))
hundreds = EnteredNum // 100
dozens = (EnteredNum % 100) // 10
unity = (EnteredNum % 100) % 10
sumOfDigits = hundreds + dozens + unity
print(sumOfDigits)
print(sumOfDigits // 3)
print(sumOfDigits % 3)
print(not(bool(sumOfDigits % 3)))
