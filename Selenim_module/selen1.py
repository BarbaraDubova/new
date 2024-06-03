import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
 
# Инициализируем драйвер браузера 
driver = webdriver.Chrome() 
 
try: 
    # Открываем страницу 
    driver.get('https://erikdark.github.io/Qa_autotest_01/') 
    time.sleep(2) 
     
    # Находим все кнопки на странице 
    buttons = driver.find_elements(By.CSS_SELECTOR, ".buttons .btn") 
     
    # Заданное количество кнопок 
    expected_button_count = 10
     
    # Фактическое количество кнопок 
    actual_button_count = len(buttons) 
     
    # Сравниваем фактическое количество с заданным и выводим результат 
    if actual_button_count == expected_button_count: 
        print(f"Количество кнопок совпадает: {actual_button_count}") 
    else: 
        print(f"Количество кнопок не совпадает: {actual_button_count} (ожидалось: {expected_button_count})") 
     
    # Находим и нажимаем третью кнопку 
    if actual_button_count >= 3: 
        btn = buttons[2] 
        btn.click() 
        time.sleep(5) 
 
finally: 
    driver.quit()
