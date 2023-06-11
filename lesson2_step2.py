from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Dima")
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("Semenov")
    email_1 = browser.find_element(By.NAME, 'email')
    email_1.send_keys("xxx@mail.ru")
    sub = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    sub.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

