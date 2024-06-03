import re

user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}

def regist(name, email, password):
# правильность ввода почты   
    if not re.match(r'[^@]+\.[^@]+', email):
        return "Некорректный email"
#наличие почты в базе
    if email in user_database:
        return 'почта уже есть'
# имя
    if not name:
        return 'поле с именем обязательно'
    if len(name) < 2:
        return 'Имя должно содержать не менее 2 букв'
#пароль
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

# рега
    user_database[email] 
    return f"Пользователь {name} зарегистрирован"

name = input("Введите ваше имя: ")
email = input("Введите ваш email: ")
password = input("Введите ваш пароль: ")

result = regist(name, email, password)
print(result)