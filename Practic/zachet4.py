def search(sentence, word):
    return word in stroka
stroka = 'раз два три'
a = 'два'

if search(stroka, a):
    print(f"Слово '{a}' найдено в строке.")
else:
    print(f"Слово '{a}' не найдено в строке.")