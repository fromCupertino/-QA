from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")))
    assert button is not None
