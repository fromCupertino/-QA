from selenium import webdriver
import time
import math
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
button = browser.find_element_by_id('book')
button.click()
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
browser.find_element_by_id('answer').send_keys(str(y))
button = browser.find_element_by_id('solve')
button.click()
time.sleep(15)
