fib1 = fib2 = 1

n = int(input("Введите число равное количеству элементов Фибоначчи, которое вам необходимо: "))

print(fib1, end=' ')

for i in range(1, n):
    f_sum = fib1 + fib2
    fib1 = fib2
    fib2 = f_sum
    print(fib2, end=' ')
