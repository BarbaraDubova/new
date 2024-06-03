import random  
import string  

def generate_password(length):
    if not (8 <= length <= 32):
        raise ValueError("Длина пароля должна быть от 8 до 32 символов.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password = generate_password(30)
print(f"Сгенерированный пароль: {password}")