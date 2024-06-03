import random

def generate_random_phrase(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            phrases = [line.strip() for line in file if line.strip()]
        
        if phrases:
            return random.choice(phrases)
        else:
            return "Файл пуст или содержит только пробелы."
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Пример использования функции
file_path = 'phrases.txt'
print(generate_random_phrase(file_path))
