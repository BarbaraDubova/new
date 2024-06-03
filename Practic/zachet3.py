def calculator():
    try:
        n1 = float(input('Введите первое число: '))
        n2 = float(input('Введите второе число: '))
        o = input('Выберите (+, -, *, /) : ')
       
        if o not in ['+', '-', '*', '/']: #проверка на корректность ввода
            raise ValueError('Нет такой операции')
        if o == '+':
            return n1 + n2
        elif o == '-':
            return n1 - n2
        elif o == '*':
            return n1 * n2
        elif o == '/':
            if n2 == 0:
                raise ValueError('Делить на ноль нельзя')
            return n1 / n2
    except ValueError as e:
        return 'Ошибка: ' + str(e)
   
while True:
    result = calculator()
    print('Результат:', result)