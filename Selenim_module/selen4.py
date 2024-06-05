import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By





#иницилизирую драйвер браузера
driver = webdriver.Chrome()




try:
    driver.get('https://erikdark.github.io/QA_autotests_11/')
    time.sleep(1)


    driver.find_element(By.CSS_SELECTOR,'#imageInput').send_keys(r'c:\Users\AttekPC\Pictures\23232.jfif')


    driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
   




finally:
    time.sleep(5)
    driver.quit()

