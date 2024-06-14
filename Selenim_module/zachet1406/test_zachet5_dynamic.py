import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.test
def test_content(driver):
    try:
        driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
    
        button = driver.find_element(By.LINK_TEXT, "Динамический контент")
        button.click()
        time.sleep(2)
    
        # Проверить наличие кнопки "Добавить элемент"
        add = driver.find_element(By.ID, "add-element")
        assert add is not None, "Кнопка 'Добавить элемент' не найдена"
    
        # Нажать на кнопку "Добавить элемент"
        add.click()
        time.sleep(2)
    
        # Проверить наличие нового элемента с текстом "Новый элемент"
        new_element = driver.find_element(By.XPATH, "//*[text()='Новый элемент']")
        assert new_element is not None, "Новый элемент не был добавлен"
    
        # Проверить что отображается сообщение "Элемент добавлен"
        message = driver.find_element(By.ID, "content-area").text
        assert message == "Элемент добавлен", f"Ожидалось сообщение 'Элемент добавлен', но '{message}'"
        print(message)
        
    finally:
        time.sleep(3)
   
  