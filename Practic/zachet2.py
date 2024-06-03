book = {}

def add():
    name = input('имя: ')
    number = input('номер : ')
    book[name] = number
    print(f'контакт {name} добавлен')

def all_contacts():
    if not book:
        print('нет ни одного контакта')
    else:
        print('список контактов: ')
        for name, number in book.items():
            print(f"{name}: {number}")

def delete():
    name = input('введите имя контакта который нужно удалить: ')
    if name in book:
        del book[name]
        print(f'контакт {name} удален')
    else:
        print(f'контакт {name} нет в контакьах')

while True:
    print('\nВыберите действие:')
    print('1 добавить новый контакт')
    print('2 список всех контактов')
    print('3 удалить контакт')
    print('4 выход')

    choice = input('введите что хотите сделать: ')
    if choice == '1':
        add()
    elif choice == '2':
        all_contacts()
    elif choice == '3':
        delete()
    elif choice == '4':
        print('выход')
        break
    else:
     print('введите данные корректно')