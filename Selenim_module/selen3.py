import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
import re

#иницилизирую драйвер браузера
driver = webdriver.Chrome()


try:
    # Открываем веб-страницу
    driver.get('https://erikdark.github.io/QA_autotests_09/')
    
    # Ждем некоторое время, чтобы страница полностью загрузилась
    time.sleep(2)

    # Находим элементы, которые содержат значения для вычисления суммы
    num1 = int(driver.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(driver.find_element(By.CSS_SELECTOR, '#num2').text)

    # Вычисляем сумму
    result = num1 + num2

    # Находим выпадающий список
    select_element = driver.find_element(By.CSS_SELECTOR, '#answerSelect')

    # Проходим по всем опциям и выбираем нужное значение
    for option in select_element.find_elements(By.TAG_NAME, 'option'):
        if option.get_attribute('value') == str(result):
            option.click()
            break

    # Нажимаем кнопку отправить
    driver.find_element(By.CSS_SELECTOR, '#submit').click()

    # Ждем немного времени, чтобы страница обновилась и проверяем результат
    time.sleep(2)

    # Проверяем результат
    result_text = driver.find_element(By.CSS_SELECTOR, '#result').text
    if result_text == "You guessed it! Well done!":
        print("Все окей")
    else:
        print("Incorrect answer!")
        
finally:
    time.sleep(5)
    driver.quit()
