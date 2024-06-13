import select
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    driver1 = webdriver.Firefox()
    driver1.implicitly_wait(3)
    yield driver1
    driver1.quit()

def test_valid_login(driver: WebDriver):
    driver = webdriver.Chrome()
    driver.get('http://selenium1py.pythonanywhere.com/ru/')
    driver.find_element(By.LINK_TEXT, 'Предложения').click()
    for i in range(4):
        buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block")
        buttons[i].click()
    driver.find_element(By.XPATH, "//a[contains(@href, '/ru/basket/')]").click()
    driver.find_element(By.LINK_TEXT, 'Перейти к оформлению').click()
    driver.find_element(By.NAME, "username").send_keys("pups@exmaple.com")
    driver.find_element(By.NAME, "password").send_keys("pupsexmaple")
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-block btn-primary"]').click()
    driver.find_element(By.NAME, "first_name").send_keys("udydomoi")
    driver.find_element(By.NAME, "last_name").send_keys("yzje")
    driver.find_element(By.NAME, "line1").send_keys("milyidom9")
    driver.find_element(By.NAME, "line4").send_keys("ylitsa")
    driver.find_element(By.NAME, "line4").send_keys("ylitsa")
    driver.find_element(By.NAME, "postcode").send_keys("1455")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary"]').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-lg"]').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-lg btn-block"]').click()
    driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-block btn-lg"]').click()
        
    # Click the continue button
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary").click()
finally:
    # Close the WebDriver
driver.quit()