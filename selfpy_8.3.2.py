# 8.3.2
#################
import datetime
from datetime import date
dictionary = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}

chosen_number = int(input('Please enter a number between 1 to 7:'))
if chosen_number == 1:
    print(dictionary['last_name'])
elif chosen_number == 2:
    print((dictionary['birth_date']).split('.')[1])
elif chosen_number == 3:
    print(len(dictionary['hobbies']))
elif chosen_number == 4:
    print(dictionary['hobbies'][-1])
elif chosen_number == 5:
    dictionary['hobbies'] = 'Cooking'
    print(dictionary)
elif chosen_number == 6:
    day = dictionary['birth_date'].split('.')[0]
    month = dictionary['birth_date'].split('.')[1]
    year = dictionary['birth_date'].split('.')[2]
    print(tuple([day, month, year]))
elif chosen_number == 7:
    today = date.today()
    today_str = today.strftime("%d/%m/%Y")
    year = today_str.split('/')[2]
    dictionary['age'] = str(int(year)-1970)
    print(dictionary)

    pass

