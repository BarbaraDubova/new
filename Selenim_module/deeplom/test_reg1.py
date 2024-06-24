import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
 
 
@pytest.fixture 
def setup_driver(): 
    driver = webdriver.Chrome() 
    yield driver 
    driver.quit() 
 
 
@pytest.fixture 
def open_registration_form(setup_driver): 
    driver = setup_driver 
    driver.get("https://erikdark.github.io/QA_DIPLOM/") 
 
    registration_link = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.LINK_TEXT, "Регистрация")) 
    ) 
    registration_link.click() 
 
 
def test_registration_validation(setup_driver, open_registration_form): 
    driver = setup_driver 
 
    name_input = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "name")) 
    ) 
    email_input = driver.find_element(By.ID, "email") 
    password_input = driver.find_element(By.ID, "password") 
    confirm_password_input = driver.find_element(By.ID, "confirmPassword") 
    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']") 
 
    # Ввод данных для регистрации 
    name_input.send_keys("Dgdfg-Ffgfg") 
    email_input.send_keys("qff1@example.com") 
    password_input.send_keys("Asdshd123") 
    confirm_password_input.send_keys("Asdshd123") 
 
    # Клик по кнопке регистрации 
    register_button.click() 
 
    try: 
        # Проверка сообщения о регистрации 
        message = WebDriverWait(driver, 20).until( 
            EC.presence_of_element_located((By.ID, "register-message")) 
        ).text 
 
        assert message == "Пользователь зарегистрирован", f"Ожидалось 'Пользователь зарегистрирован', получено '{message}'" 
 
        # Проверка имени 
        assert all(char.isalpha() or char == '-' for char in name_input.get_attribute('value')), "Имя должно содержать только буквы и символ '-'" 
 
        # Проверка email 
        assert '@' in email_input.get_attribute('value') and '.' in email_input.get_attribute('value'), "Некорректный формат email" 
 
        # Проверка пароля 
        password = password_input.get_attribute('value') 
        assert len(password) >= 8, "Пароль должен содержать не менее 8 символов" 
        assert any(char.isupper() for char in password), "Пароль должен содержать хотя бы одну заглавную букву" 
        assert any(char.islower() for char in password), "Пароль должен содержать хотя бы одну строчную букву" 
        assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру" 
         
        # Проверка совпадения пароля и его подтверждения 
        assert password == confirm_password_input.get_attribute('value'), "Пароли не совпадают" 
 
    finally: 
        driver.quit()