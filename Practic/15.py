def number(phone_number):
    return len(phone_number) == 12 and phone_number.startswith('+') and phone_number[1:].isdigit()

def a():
    phone_number = input("Введите номер телефона в формате +XXXXXXXXXXX: ")
    if number(phone_number):
        print('Номер правильный')
    else:
        print('Номер неправильный')
a()