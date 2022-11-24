a = input('Введите первое число')
b = input('Введите второе число')
n = int(input('Введите третье число'))
try:
    c = int(a) + int(b)
    print(f'1 число + 2 число = : {c} ')
except ValueError:
    print('Не удалось преобразовать строку в int')
    try:
        c = a + n
        print(f'1 число + 3 число = : {c} ')
    except TypeError:
        print('Разные типы нельзя складывать')

