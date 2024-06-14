import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.test
def  test_registration(driver):
    driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
    registration_link = driver.find_element(By.LINK_TEXT, "Регистрация")
    registration_link.click()
    time.sleep(2)
  
    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    
    name_input.send_keys("TestTestovich")
    email_input.send_keys("tesst@example.com")
    password_input.send_keys("pass112424")

    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    register_button.click()
    time.sleep(2)
    
    message = driver.find_element(By.ID, "register-message").text
    assert message == "Пользователь зарегистрирован", f"Ожидалось сообщение 'Пользователь зарегистрирован', но '{message}'"
    print(message)