"""
Дата 10 июня 1960 года является особенной, потому что если ее записать в приведенном ниже формате,
то произведение дня и месяца равняется году:
10.06.60
Разработайте программу, которая просит пользователя ввести месяц (в числовой форме),
день и двузначный год. Затем программа должна определить, равняется ли произведение
дня и месяца году. Если это так, то она должна вывести сообщение, говорящее,
что введенная дата является магической. В противном случае она должна вывести сообщение,
что дата не является магической.
"""

def is_magic_date(day, month, year):
    two_digit_year = year % 100

    if day * month == two_digit_year:
        print(f"{day}.{month}.{year} - it's a magic date")
    else:
        print('your date is not magical')


d = int(input('Enter the day of your date:'))
m = int(input('Enter the month of your date:'))
y = int(input('Enter the year of your date:'))

is_magic_date(d, m, y)

