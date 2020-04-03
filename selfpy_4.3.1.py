# 4.3.1
#################
input_word = (input('Please enter a word:'))
if input_word.isalpha() and len(input_word) > 1:
    print('E1')
elif len(input_word) == 1 and not(input_word.isalpha()):
    print('E2')
elif not(input_word.isalpha()) and len(input_word) > 1:
    print('E3')
elif input_word.isalpha() and len(input_word) == 1:
    print(input_word.lower())





