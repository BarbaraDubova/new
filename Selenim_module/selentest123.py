from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://erikdark.github.io/dovod_repo_QA_form/")

    # Установка времени ожидания
    wait = WebDriverWait(driver, 10)

    # Нахождение полей формы и кнопки
    login_field = wait.until(EC.presence_of_element_located((By.ID, 'login')))
    password_field = driver.find_element(By.ID, 'password')
    database_field = driver.find_element(By.ID, 'database')
    host_field = driver.find_element(By.ID, 'host')
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # Заполнение формы правильными данными
    login_field.send_keys('admin123')
    password_field.send_keys('password123')
    database_field.send_keys('bd_dovod')
    host_field.send_keys('localhost')

    # Отправка формы
    submit_button.click()
    
    # Ожидание 3 секунды
    wait.until(lambda driver: time.sleep(3))

    # Очистка полей
    login_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)  # Очистка поля
    password_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    database_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    host_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    # Ожидание 3 секунды перед следующим заполнением
    wait.until(lambda driver: time.sleep(3))

    # Заполнение формы перевернутыми данными после подсказки
    login_field.send_keys('321nimda')
    password_field.send_keys('321drowssap')
    database_field.send_keys('dovod_db')
    host_field.send_keys('tsohlacol')

    # Отправка формы
    submit_button.click()

    # Ожидание 3 секунды после отправки формы
    wait.until(lambda driver: time.sleep(3))

finally:
    # Закрытие браузера
    driver.quit()

    №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№


    