import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.test
def test_profile(driver):
    try:
        # Открытие страницы
        driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
        
        # Переход с главной на профиль
        profile_link = driver.find_element(By.LINK_TEXT, "Профиль")
        profile_link.click()
        time.sleep(2)
        
        # Нажатие на кнопку выхода
        button = driver.find_element(By.ID, "logout-button")
        button.click()
        time.sleep(2)
        
        # Проверка сообщения о регистрации
        message = driver.find_element(By.ID, "register-message").text
        assert message == "Пользователь зарегистрирован", f"Ожидалось сообщение 'Пользователь зарегистрирован', но '{message}'"
        print(message)

    finally:
        time.sleep(3)
