book = {}

while True:
    print('\nВыберите действие:')
    print('1 добавить новый контакт')
    print('2 список всех контактов')
    print('3 наличие контакта в книге')
    print('4 выход')

    choice = input('введите что хотите сделать: ')
    
    if choice == '1':
        name = input('имя: ')
        number = input('номер: ')
        book[name] = number
        print(f'контакт {name} добавлен')
    
    elif choice == '2':
        if not book:
            print('нет ни одного контакта')
        else:
            print('список контактов:')
            for name, number in book.items():
                print(f"{name}: {number}")
    
    elif choice == '3':
       если контакт уже был в контактах то выдать сообщение об этом
    
    elif choice == '4':
        print('выход')
        break
    
    else:
        print('введите данные корректно')