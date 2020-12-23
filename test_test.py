import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    pole = WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.TAG_NAME,'textarea')))
    pole.send_keys(str(answer))
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    alert = WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.CLASS_NAME,'smart-hints__hint')))
    assert alert.text == 'Correct!'
