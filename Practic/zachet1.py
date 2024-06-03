def a(numbers):
     result = [num for num in numbers if num % 3 == 0]
     return result

numbers = [33, 1, 12, 3, 27, 0, 10]
result = a(numbers)
print(result)