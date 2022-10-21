n = int(input('Введите возраст: '))

div = n % 10

if 10 < n < 20:
    print('ему', n, 'лет')
elif 1 < div < 5:
    print('ему', n, 'года')
elif div == 1:
    print('ему', n, 'год')
else:
    print('ему', n, 'лет')