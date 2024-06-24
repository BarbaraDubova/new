import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def open_magaz_form(setup_driver):
    driver = setup_driver
    driver.get("https://erikdark.github.io/QA_DIPLOM/")

    magaz_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Магазин"))
    )
    magaz_link.click()

    return driver

def test_add_to_cart(open_magaz_form):
    driver = open_magaz_form

    # для сверки
    products = [
        {"name": "Товар 1", "price": 100},
        {"name": "Товар 2", "price": 200},
        {"name": "Товар 3", "price": 300}
    ]

    # добавление в корзину
    for product in products:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@data-name='{product['name']}']"))
        )
        add_button.click()

        time.sleep(2)


        alert = driver.switch_to.alert
        assert f"{product['name']} добавлен в корзину" in alert.text
        alert.accept()

    # проверка что товары добавлены
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartButton"))
    )
    cart_button.click()

    time.sleep(2)

    cart_items = driver.find_elements(By.XPATH, "//div[@id='cartItems']/div")
    assert len(cart_items) == len(products)

    # Проверка: если товар добавлен несколько раз, он отображается соответствующее количество раз
    for product in products:
        item_text = f"{product['name']} - ${product['price']}"
        count = sum(1 for item in cart_items if item.text == item_text)
        # поверка одноразового добавления товара
        assert count == 1 

    # схожесть цены в корзине с ценой товара
    total_in_cart = driver.find_element(By.ID, "cartTotal").text
    expected_total = sum(product['price'] for product in products)
    assert f"Общая стоимость: ${expected_total}" in total_in_cart
  