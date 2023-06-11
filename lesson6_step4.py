from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    galochka = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", galochka)
    galochka.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    sub = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    sub.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла