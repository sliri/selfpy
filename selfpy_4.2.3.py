# 4.2.3
#################
input_temp = (input('Insert the temperature you would like to convert:'))
input_temp_int = float(input_temp[:len(input_temp)-1])
if input_temp.endswith('C') or input_temp.endswith('c'):
    converted = (9*input_temp_int + (32*5))/5
    print(converted, 'F')
elif input_temp.endswith('F') or input_temp.endswith('f'):
    converted = (5 * input_temp_int - 160) / 9
    print(converted, 'C')
else:
    print('Input Not Valid!')
