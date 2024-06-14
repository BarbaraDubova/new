import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()
    yield driver
    # Закрытие драйвера после завершения всех тестов
    driver.quit()

def pytest_configure(config):
    config.addinivalue_line("markers", "test: mark a test function")