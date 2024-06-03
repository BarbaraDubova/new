try:
    a1 = float(input('Введите первое число: '))
    a2 = float(input('Введите второе число: '))
    result = a1 / a2
    print('Результат:', result)
except ZeroDivisionError:
    print('Ошибка: деление на ноль')
except ValueError:
    print('Ошибка: введено не число')
