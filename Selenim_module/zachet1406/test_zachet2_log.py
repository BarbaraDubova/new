import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.test
def test_loginn(driver):
    driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
    login = driver.find_element(By.LINK_TEXT, "Логин")
    login.click()
    time.sleep(2)
    
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    
    email_input.send_keys("test@gmail.com")
    password_input.send_keys("pass2343423")
    
    # Нажатие кнопки "Войти"
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Ожидание сообщения о входе
    time.sleep(2)
    
    # Проверка сообщения о входе
    message = driver.find_element(By.ID, "login-message").text
    assert message == "Пользователь вошел в систему", f"Ожидалось сообщение 'Пользователь вошел в систему', но '{message}'"
    print(message)
