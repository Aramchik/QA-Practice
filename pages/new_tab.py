
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage


# Lockators
# new tab link locators
link = (By.XPATH, "//a[@id='new-page-link']")
result_text = (By.XPATH, '//p[@id="result-text"]')

# new tab button lockators
click_button = (By.XPATH, '//a[@id="new-page-button"]')



# Class for New tab page
class NewTabPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)




    # Open New tab link page
    def open_new_tab_link_page(self):
        self.browser.get("https://www.qa-practice.com/elements/new_tab/link")


    # Open New tab page
    def open_new_tab_button_page(self):
        self.browser.get("https://www.qa-practice.com/elements/new_tab/button")



        # Getters
    # getters new tab link

    def get_link(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(link))


    def get_result_text(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(result_text))






    # getters new tab button
    def get_click_button(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(click_button))






        # Actions
    # new tab link actions
    def click_link(self):
        self.get_link().click()





    # new tab button actions
    def click_click_button(self):
        self.get_click_button().click()



        # Asserts

    def assert_result_text(self):
        self.assert_values(self.get_result_text(),"I am a new page in a new tab")
        print('Test done')