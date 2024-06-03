questions = {
    "столица австралии": "канберра",
    "сколько океанов в мире": "5",
    "название кривого здания во франции": "пизанская башня"
}
def quiz(questions):
    score = 0 
    
    for question, answer in questions.items(): #пара ключ знач
        user = input(question + " ") #запрос ответа
        if user.lower() == answer.lower(): #проверка ответа
            score += 1 #увеличение счетчика при правильном отв
    
    print("\nрезультат:")
    print(f"отвечено правильно: {score} из {len(questions)}")
quiz(questions)


    

