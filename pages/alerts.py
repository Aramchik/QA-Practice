from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage


    # Alerts Lockators'
# Alert box
click_1 = (By.CLASS_NAME, "a-button")

# Confirmation box
click_2 = (By.CLASS_NAME, "a-button")
result_text = (By.ID, "result-text")

# Prompt box
click_3 = (By.CLASS_NAME, "a-button")


# Class for Alerts
class Alerts(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open Alerts Alert box page
    def open_alert_box_page(self):
        self.browser.get("https://www.qa-practice.com/elements/alert/alert")



    # Open Alert Confirmation box
    def open_confirmation_box_page(self):
        self.browser.get("https://www.qa-practice.com/elements/alert/confirm")



    # Open Alert Promt box
    def open_alert_promt_box_page(self):
        self.browser.get("https://www.qa-practice.com/elements/alert/prompt")





        # Getters
    # Getter click_1 on Alert box Page
    def get_first_button(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(click_1))



    # Getter click_2 on Confirmation box Page
    def get_second_button(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(click_2))



    # Getter result text
    def get_result_text(self):
        return WebDriverWait(self.browser,10).until(Ec.visibility_of_element_located(result_text))



    # Getter click_3 on Promt box Page
    def get_third_button(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(click_3))





        # Asserts
    # Asert result text if choice Ok
    def assert_result_text_ok(self):
        self.assert_values(self.get_result_text(),'Ok')
        print('You selected ok')



    # Asert result text if choice Cancel
    def assert_result_text_cancel(self):
        self.assert_values(self.get_result_text(), 'Cancel')
        print('You selected Cancel')



    # Asert result text if some typing text
    def assert_result_text_typing(self):
        self.assert_values(self.get_result_text(), 'Some text')
        print('You entered Some text')





        # Actions
    # Click first button on Alert box Page
    def click_1(self):
        self.get_first_button().click()
        print('Click first button')



    # Click second button on Confirmation box Page
    def click_2(self):
        self.get_second_button().click()
        print('Click second button')




    # Click third button on Promt box Page
    def click_3(self):
        self.get_third_button().click()
        print('Click third button')







