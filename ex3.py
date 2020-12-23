import unittest
import time


class Test(unittest.TestCase):
    def test_1(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('test')
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('test')
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('test')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_2(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('test')
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('test')
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('test')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


# ожидание чтобы визуально оценить результаты прохождения скрипта
if __name__ == "__main__":
    unittest.main()
    time.sleep(10)

# закрываем браузер после всех манипуляций
