def a(email):
    return '@' in email and '.' in email and email.index('@') < email.index('.')

# Ввод email через терминал
email = input('Введите почту: ')

if a(email):
    print('корректен')
else:
    print('Email некорректен')