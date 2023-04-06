#Найти все числа, кратные 11, в диапазоне от 0 до 10000

for i in range(0,10000):
    if i % 11 == 0:
        print(i)
#     if i%11 !=0:
#         continue
#     print(i)