from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage

# Lockators

single_ui_elements = (By.XPATH, "//*[@id='sidebar']/div/ul/li[2]")




# Class for Main page
class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open home page
    def open_main_page(self):
        self.browser.get("https://www.qa-practice.com/")



    # Getters

    def get_suie(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(single_ui_elements))


    # Actions

    def click_suie(self):
        self.get_suie().click()
        print('Drop down clicked')