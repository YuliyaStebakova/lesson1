str1 = '123'
new = int(str1)
print(type(new))


while True:
    print("Введите дату рождения первого человека(год, месяц, день)", end=' ')
    year, month, day = map(int,input().split())
    print("Введите дату рождения второго человека(год, месяц, день)", end=' ')
    year2, month2, day2 = map(int,input().split())
    age_first = (2022-year)*365+month*30+day2
    age_second = (2022-year2)*365+month2*30+day2
    if age_first > age_second:print("Первый старше на", age_first-age_second, "дней")
    else:print("Второй старше на", age_second-age_first, "дней")















# buy = 1
# a1 = 5
# b = 1.6
# b1 = 3.8
# c = 'dad'
# c1 = 'mom'
# f = None
# d = True
# d1 = False
# print(buy, a1, b, b1, c, c1, f, d, d1)
# print(f)
# print(c)
# print(a1)