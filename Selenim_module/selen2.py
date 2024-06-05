import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера браузера
driver = webdriver.Chrome()

driver.get("https://erikdark.github.io/Qa_autotest_07/")

try:
    # Ждем несколько секунд, чтобы страница успела загрузиться полностью
    time.sleep(4)
    
    # Извлекаем первое число, которое генерируется на сайте
    big_number_text = driver.find_element(By.CLASS_NAME, "big-number").text
    first_number = int(big_number_text.split()[-1])
    
    # Проверяем, есть ли второе число в атрибуте data-b изображения
    second_number = None
    data_b_value = driver.find_element(By.ID, "numberImage").get_attribute("data-b")
    for char in data_b_value:
        if char.isdigit():
            second_number = int(char)
            break
    
    # Если второе число найдено, вычисляем сумму и вводим ответ в форму
    if second_number is not None:
        sum_result = first_number + second_number
        answer_input = driver.find_element(By.ID, "answer")
        answer_input.send_keys(str(sum_result))
        
        # Нажатие кнопки "Отправить"
        submit_button = driver.find_element(By.ID, "submitBtn")
        submit_button.click()
  

  
    time.sleep(4)


finally:
    # Закрываем браузер после выполнения задачи
    driver.quit()