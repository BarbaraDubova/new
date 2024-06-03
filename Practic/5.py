try:
       with open(r'C:\Users\AttekPC\Desktop\QA_V\new\Practic\практика 1305.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('Ошибка открытия файла')