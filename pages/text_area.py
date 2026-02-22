from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage
import time

# Lockators
submit_button = (By.XPATH, "//input[@id='submit-id-submit']")

# text area locators
text_area_input = (By.XPATH, "//textarea[@id='id_text_area']")
result_text = (By.XPATH, '//p[@id="result-text"]')


# text area multi lockators
first_chapter = (By.XPATH, '//textarea[@id="id_first_chapter"]')
second_chapter = (By.XPATH, '//textarea[@id="id_second_chapter"]')
third_chapter = (By.XPATH, '//textarea[@id="id_third_chapter"]')




# Class for New tab page
class TextArea(BasePage):
    def __init__(self, browser):
        super().__init__(browser)




    # Open Text area page
    def open_text_area_page(self):
        self.browser.get("https://www.qa-practice.com/elements/textarea/single")

    # Open multi text area page
    def open_multi_text_area_page(self):
        self.browser.get("https://www.qa-practice.com/elements/textarea/textareas")




        # Getters
    def get_submit_button(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(submit_button))


    # getters text area
    def get_text_area_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(text_area_input))

    def get_result_text(self):
        #result_elem = WebDriverWait(self.browser, 30).until(Ec.presence_of_element_located(result_text))  # сначала присутствует в DOM
        #self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", result_elem)
        #time.sleep(2)  # даём JS время отрендерить
        #WebDriverWait(self.browser, 10).until(
        #lambda driver: result_elem.is_displayed() and len(result_elem.text.strip()) > 0)
        #text = result_elem.text.strip()
        #print(f"Получен текст результата: '{text}'")  # для отладки в CI
        #return text
        return WebDriverWait(self.browser,10).until(Ec.visibility_of_element_located(text_area_input))



    # getters multi text area
    def get_first_chapter(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(first_chapter))

    def get_second_chapter(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(second_chapter))

    def get_third_chapter(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(third_chapter))






        # Actions
    # function for do small page
    def do_small(self):
        self.get_result_text().send_keys(Keys.CONTROL, "-")
        self.get_result_text().send_keys(Keys.CONTROL, "-")

    # text area actions

    def typing_text(self):
        self.get_text_area_input().send_keys('Some text')
        print('Text typing')


    def click_submit(self):
        # Находим элемент (WebElement)
        submit_btn = self.get_submit_button()  # это WebElement, а не локатор
        # Прокручиваем
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",submit_btn)  # ← передаём WebElement
    
        time.sleep(1.5)
    
        # Ждём кликабельности
        WebDriverWait(self.browser, 15).until(Ec.element_to_be_clickable(submit_btn))
        
        # Пробуем обычный клик
        try:
            submit_btn.click()
            print("Обычный клик прошёл")
        except Exception as e:
            print(f"Обычный клик упал: {e}")
            # Клик через JS — передаём WebElement
            self.browser.execute_script("arguments[0].click();", submit_btn)
            print("Клик через JS прошёл")
        
            # Даём время на обработку submit
            time.sleep(2)



    # text area multi actions
    def typing_first_text(self):
        self.get_first_chapter().send_keys('first chapter text')
        print('First chapter typing')

    def typing_second_text(self):
        self.get_second_chapter().send_keys('second chapter text')
        print('Second chapter typing')

    def typing_third_text(self):
        self.get_third_chapter().send_keys('third chapter text')
        print('Third chapter typing')



        # Asserts
    # Text area asserts
    def assert_text_area_input(self):
        self.assert_values(self.get_result_text(),'Some text')
        print('Text good')


    # Multi text area asserts
    # only first chapter assert
    def assert_first_text_area(self):
        self.assert_values(self.get_result_text(),'First chapter text')
        print('Text good')



    # first and second chapter assert
    def assert_first_and_second_text_area(self):
        self.assert_values(self.get_result_text(), 'First chapter text\nSecond chapter text')
        print('Text good')



    # first second and third chapter assert
    def assert_first_second_third_text_area(self):
        self.assert_values(self.get_result_text(), 'First chapter text\nSecond chapter text\nThird chapter text')
        print('Text good')



    # first and third chapyter assert
    def assert_first_third_text_area(self):
        self.assert_values(self.get_result_text(), 'First chapter text\nThird chapter text')
        print('Text good')
