def a(password):

  

    
     def password(passwordd):
    # Проверка длины
      a = len(password) >= 8

    # на заглавную
      b = any(char.isupper() for char in password)

    # на цифры
      v = any(char.isdigit() for char in password)

    # на символы
      d = any(char in '!@#$%^&*()_+{}[]:";\'<>,.?/' for char in password)

    # Общий результат проверки
      return a and b and v and d

password = input('введите пароль ')
if a(password):
    print('пароль хороший')
else:
    print('пароль нужно переделать под условия')

    