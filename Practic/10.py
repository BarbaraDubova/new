
import random  

def generate(file_path):
    with open(r'C:\Users\AttekPC\Desktop\QA_V\new\Practic\практика 1305.txt', 'r', encoding='utf-8') as file: 
        a = file.read().splitlines()
    return random.choice(a) if a else 'пустой файл'


file_path = r'C:\Users\AttekPC\Desktop\QA_V\new\Practic\практика 1305.txt'  
print(generate(file_path))