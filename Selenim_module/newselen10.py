import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def login(driver, username, password):
    driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
    
    # Открытие модального окна
    open_modal_button = driver.find_element(By.ID, 'openModalButton')
    open_modal_button.click()
    
    # Ожидание появления модального окна
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'loginModal'))
    )

    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    if username:
        username_input.send_keys(username)
    if password:
        password_input.send_keys(password)

    login_button.click()

@pytest.mark.parametrize("username,password,expected_message", [
    ("testuser", "password123", None),  # Успешный логин
    ("wronguser", "password123", "Invalid username or password."),  # Неправильный логин
    ("testuser", "wrongpassword", "Invalid username or password."),  # Неправильный пароль
    ("testuser", "", "Password is required."),  # Пароль не указан
    ("", "password123", "Username is required.")  # Логин не указан
])
def test_login(driver, username, password, expected_message):
    login(driver, username, password)
    
    if expected_message is None:
        # Проверка успешного входа и закрытия модального окна
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, 'loginModal'))
        )
        assert "Dashboard" in driver.title  # Предполагаем, что заголовок страницы меняется на Dashboard
    else:
        # Проверка сообщений об ошибках
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-message'))
        )
        assert error_message.text == expected_message