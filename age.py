years = int(input('Введите год рождения: '))
month = int(input('Введите месяц рождения: '))
day = int(input('Введите день рождения: '))
years_now = int(input('Введите сегодняшний год: '))
month_now = int(input('Введите сегодняшний месяц: '))
day_now = int(input('Введите сегодняшний день: '))

s = years_now - years

if month_now < month:
   s -= 1
elif month_now == month and day_now < day:
    s -= 1

print(s)