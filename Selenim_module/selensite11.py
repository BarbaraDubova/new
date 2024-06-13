import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация WebDriver
driver = webdriver.Chrome()

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Открытие сайта
    driver.get("http://selenium1py.pythonanywhere.com/ru/")
    
    # Клик на ссылку "Предложения"
    driver.find_element(By.LINK_TEXT, "Предложения").click()
    
    for i in range(4):
        buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
        buttons[i].click()
    
    # Переход в корзину
    driver.find_element(By.LINK_TEXT, "Посмотреть корзину").click()
    
    # Начало оформления заказа
    driver.find_element(By.LINK_TEXT, "Перейти к оформлению").click()
    
    # Ввод адреса
    driver.find_element(By.ID, "id_username").send_keys("sssnakeee@gmail.com")
    
  
    driver.find_element(By.ID, "id_options_1").click()
    
    # 
    driver.find_element(By.ID, "id_password").send_keys("FfFjkl123!")
    
    # 
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-block.btn-primary").click()
    
    # 
    driver.find_element(By.ID, "id_password1").send_keys("FfFjkl123!")
    driver.find_element(By.ID, "id_password2").send_keys("FfFjkl123!")
    
    # 
    driver.find_element(By.CSS_SELECTOR, "button[name='registration_submit']").click()
    
    # 
    driver.find_element(By.ID, "id_first_name").send_keys("AAAAAA")
    driver.find_element(By.ID, "id_last_name").send_keys("AAAAAABB")
    driver.find_element(By.ID, "id_line1").send_keys("Спасская дом 1 корпус 1")
    driver.find_element(By.ID, "id_line4").send_keys("Питер")
    driver.find_element(By.ID, "id_postcode").send_keys("198266")
    driver.find_element(By.ID, "id_phone_number").send_keys("+79219898991")
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary").click()

finally:
    # Close the WebDriver
    driver.quit()