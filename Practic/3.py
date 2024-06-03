with open(r'C:\Users\AttekPC\Desktop\QA_V\new\Practic\практика 1305.txt', 'r', encoding='utf-8') as file: 
    text = file.read()
if 'Рэдрик' in text:
    print("Слово  найдено")
else:
    print("Слово не найдено")
