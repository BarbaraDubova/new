def test_calc(operator, n1, n2):
    try:
        if operator == '+':
            result = n1 + n2
        elif operator == '-':
            result = n1 - n2
        elif operator == '*':
            result = n1 * n2
        elif operator == '/':
            if n2 == 0:
                raise ZeroDivisionError('нельзя делить на ноль')
            result = n1 / n2
        else:
            raise ValueError('неправильный оператор')
        return result
    except ZeroDivisionError as a:
        return str(a)
    except ValueError as a:
        return str(a)
    
#print(test_calc('+', 5, 3))  # Вывод: 8
#print(test_calc('-', 8, 2))  # Вывод: 6
#print(test_calc('*', 4, 6))  # Вывод: 24
#print(test_calc('/', 10, 2)) # Вывод: 5.0
#print(test_calc('/', 5, 0))  # Вывод: Деление на 0 недопустимо
print(test_calc('%', 5, 2))  # Вывод: Неправильно указан оператор