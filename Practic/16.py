def a(text, max):
    return len(text) <= max

# Пример использования:
text = "аыраыр"
max = 20

if a(text, max):
    print('длина в норме')
else:
    print('превышение длины')