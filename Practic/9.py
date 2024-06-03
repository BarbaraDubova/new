def a(number):
    number_str = str(number)
    total = sum(int(digit) for digit in number_str)
    return total

number = 12345
print(a(number))