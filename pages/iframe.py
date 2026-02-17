from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage


# Lockators

navbar = (By.XPATH, "//span[@class='navbar-toggler-icon']")
iframe = (By.XPATH, '//iframe[@class="embed-responsive-item"]')



# Class for Iframe page
class Iframe(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Open iframe page
    def open_iframe_page(self):
        self.browser.get("https://www.qa-practice.com/elements/iframe/iframe_page")




    # Getters

    # Getter navnbar
    def get_navbar(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(navbar))


    # getter iframe
    def get_iframe(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(iframe))


    # Actions
    # function for switch to iframe
    def switch_to_iframe(self):
        WebDriverWait(self.browser, 10).until(Ec.frame_to_be_available_and_switch_to_it(self.get_iframe()))
        print("Switch to iframe")



    # Function for click navbar
    def click_navbar(self):
        self.get_navbar().click()
        print('Click navbar')