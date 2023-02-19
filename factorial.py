n = int(input("Введите натуральное число: "))

factorial = 1
for i in range(n):
    factorial = factorial * n
    n -= 1
print(factorial)
