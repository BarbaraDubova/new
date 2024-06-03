import random

joke_templates = [
    'Почему {} перешел дорогу?',
    'Почему {} катится вниз?',
    'Потому что {} смеется над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились?'
]

joke_elements = [
    'слон', 'заяц', 'бетмен', 'крокодил', 'чебурашка', 'студент', 
    'препод', 'водитель', 'улитка'
]

def generate_joke():
    
    a = random.choice(joke_templates)
    num_elements = a.count('{}')
    elements = random.sample(joke_elements, num_elements)
    joke = a.format(*elements)
    return joke

print(generate_joke())