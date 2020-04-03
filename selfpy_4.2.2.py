# 4.2.2
#################
input_word = (input('Please enter a word:')).lower()
input_length = len(input_word)
if input_word[0::1] == input_word[-1::-1]:
    print('O.K')
else:
    print('Not')
