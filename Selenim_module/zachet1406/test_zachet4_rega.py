import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.test
def test_tabli(driver):
    try:
        # Открытие страницы
        driver.get("https://erikdark.github.io/zachet_selenium_01/index.html")
        
        # Переход на таблицу данных
        button = driver.find_element(By.LINK_TEXT, "Таблица данных")
        button.click()
        time.sleep(2)

        # Функция для получения данных из колонки
        def get_column_data(column_index):
            rows = driver.find_elements(By.CSS_SELECTOR, "#data-table tbody tr")
            return [row.find_elements(By.TAG_NAME, "td")[column_index].text for row in rows]

        # Функция для проверки сортировки по колонке
        def check_sort(column_index):
            # Сохранение исходных данных
            original_data = get_column_data(column_index)
            
            # Нажатие для сортировки
            header = driver.find_elements(By.CSS_SELECTOR, "#data-table th")[column_index]
            header.click()
            time.sleep(2)

            # Получение отсортированных данных
            sorted_data = get_column_data(column_index)

            # Проверка сортировки
            assert sorted_data == sorted(original_data), f"Данные в колонке {column_index} не отсортированы"
            
            # Проверка сообщения о сортировке
            message = driver.find_element(By.ID, "sort-message").text
            expected_message = f"Таблица отсортирована по столбцу {column_index + 1}"
            assert message == expected_message, f"Ожидалось сообщение '{expected_message}', но '{message}'"
            print(message)

        # Проверка сортировки для каждой из трех колонок
        check_sort(0)
        check_sort(1)
        check_sort(2)

    finally:
        time.sleep(3)











