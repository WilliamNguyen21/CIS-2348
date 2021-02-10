#William Nguyen
#1824617
cmonth = input('Enter current Month: ')
cday = input('Enter current day: ')
cyear = input('Enter current year: ')
bmonth = input('Enter Birthday Month: ')
bday = input('Enter Birthday day: ')
byear = input('Enter Birthday year: ')
age = int(cyear) - int(byear)
if int(cmonth) < int(bmonth):
    age = age-1
if int(cmonth) == int(bmonth):
    if int(cday) < int(bday):
        age = age-1

print('Birthday Calculator')
print('Current day')
print('Month:', cmonth)
print('Day:',  cday)
print('Year:',  cyear)
print('Birthday')
print('Month:', bmonth)
print('Day:',  bday)
print('Year:',  byear)
print('You are', age, 'years old.')

if int(cmonth) == int(bmonth) and int(cday) == int(bday):
    print('Happy Birthday!')