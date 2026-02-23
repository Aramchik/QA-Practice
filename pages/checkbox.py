from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage
import time

# Lockators
# Single checkbox lockators
select_checkbox = (By.XPATH, "//input[@id='id_checkbox_0']")
submit_button = (By.XPATH, "//input[@id='submit-id-submit']")
selected_text = (By.XPATH, "//p[@id='result-text']")


# Checkboxes lockators
one_checkbox = (By.XPATH, "//input[@id='id_checkboxes_0']")
two_checkbox = (By.XPATH, "//input[@id='id_checkboxes_1']")
three_checkbox = (By.XPATH, "//input[@id='id_checkboxes_2']")







# Class for Main page
class CheckboxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open simple checkbox page
    def open_simple_checkbox_page(self):
        self.browser.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")

    # Open simple checkbox page
    def open_checkboxs_page(self):
        self.browser.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")






    # Getters
    # Single checkbox getters

    def get_select_checkbox(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(select_checkbox))

    def get_submit_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(submit_button))
    def get_selected_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(selected_text))






    # Checkbox getters
    def get_one_checkbox(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(one_checkbox))

    def get_two_checkbox(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(two_checkbox))

    def get_three_checkbox(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(three_checkbox))



    # Actions
    # Single checkbox actions
    def click_select_checkbox(self):
        self.get_select_checkbox().click()


    def click_submit_button(self):
        self.get_submit_button().click()
        print('Click submit button')


    def assert_selected_text(self):
        self.assert_values(self.get_selected_text(),"select me or not")
        print("selected text is good")




    # Checkboxs actions
    def click_one(self):
        self.get_one_checkbox().click()

    def click_two(self):
        self.get_two_checkbox().click()

    def click_three(self):
        self.get_three_checkbox().click()








    # Only one

    def only_one(self):
        self.click_one()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'one')
        time.sleep(1)
        print('checkbox one is correct')





    # Only two

    def only_two(self):
        self.click_two()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'two')
        time.sleep(1)
        print('checkbox two is correct')





    # Only three

    def only_three(self):
        self.click_three()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'three')
        time.sleep(1)
        print('checkbox three is correct')




    # One and two

    def one_two(self):
        self.click_one()
        time.sleep(1)
        self.click_two()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'one, two')
        time.sleep(1)
        print('checkbox one and two is correct')



    # One and three

    def one_three(self):
        self.click_one()
        time.sleep(1)
        self.click_three()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'one, three')
        time.sleep(1)
        print('checkbox one and three is correct')




    # two and three

    def two_three(self):
        self.click_two()
        time.sleep(1)
        self.click_three()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'two, three')
        time.sleep(1)
        print('checkbox two and three is correct')




    # all

    def all(self):
        self.click_one()
        time.sleep(1)
        self.click_two()
        time.sleep(1)
        self.click_three()
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
        self.assert_values(self.get_selected_text(), 'one, two, three')
        time.sleep(1)
        print('checkbox one, two, three is corect')
