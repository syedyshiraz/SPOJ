from datetime import date
print('enter your date of birth details: ')
d=int(input('enter date: '))
m=int(input('enter month: '))
y=int(input('enter year: '))
age=date.today()-date(y,m,d)
age_in_sec=age.days*24*60*60
print("you have lived",age_in_sec,"secs")
