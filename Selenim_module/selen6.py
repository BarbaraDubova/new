
import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re

# Инициализация драйвера браузера
driver = webdriver.Chrome()


try:
    # Открытие страницы
    driver.get("https://erikdark.github.io/QA_autotests_13/")

    # Нажатие на кнопку для открытия новой вкладки
    button = driver.find_element(By.ID, "openNewPageBtn")
    button.click()

    # Переключение на новую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавим задержку в 2 секунды, чтобы дать странице загрузиться
    time.sleep(2)

    # Нажатие на кнопку на новой вкладке
    button_new_tab = driver.find_element(By.ID, "displayTextBtn")
    button_new_tab.click()

    # Добавим еще одну задержку в 2 секунды, чтобы дать алерту появиться
    time.sleep(2)

    # Подтверждение алерта
    alert = driver.switch_to.alert
    alert.accept()

    # Проверка текста алерта
    alert_text = alert.text
    if alert_text == "Хорошо!":
        print("Текст алерта совпадает с ожидаемым.")
    else:
        print("Текст алерта не совпадает с ожидаемым.")

finally:
    time.sleep(5)
    driver.quit()
