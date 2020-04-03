# 4.2.4
#################
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
week_days_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
input_date = (input(' Enter a date:')).rsplit('/')
weekday = (calendar.weekday(int(input_date[2]), int(input_date[1]), int(input_date[0])))
print(week_days_list[weekday])

