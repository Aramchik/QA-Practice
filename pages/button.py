from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage

# Lockators
# Simple button lockators
simple_button_click = (By.XPATH, "//input[@id='submit-id-submit']")
click_text = (By.XPATH, "//p[@id='result-text']")


# disabled button lockators
select_state = (By.XPATH, "//select[@id='id_select_state']")

disabled_status = (By.XPATH, "//option[@value='disabled']")
enabled_status = (By.XPATH, "//option[@value='enabled']")

submit_button = (By.XPATH, "//input[@id='submit-id-submit']")
submit_text = (By.XPATH, "//p[@id='result-text']")




# Class for Main page
class ButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open simple button page
    def open_simple_button_page(self):
        self.browser.get("https://www.qa-practice.com/elements/button/simple")



    # Open disabled button page
    def open_disabled_button_page(self):
        self.browser.get("https://www.qa-practice.com/elements/button/disabled")





            # Getters
        # Simple button klick getters
    # Getter simple button click
    def get_simple_button_click(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(simple_button_click))


    # getter text after click click button
    def get_click_text(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(click_text))






        # Disabled button klick getters
    # getter select state drag n drop
    def get_select_state(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(select_state))


    # Getter disabled
    def get_disabled_status(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(disabled_status))


    # getter enabled
    def get_enabled_status(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(enabled_status))



    # getter submit button
    def get_submit_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(submit_button))



    # getter submit text after click submit
    def get_submit_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(submit_text))





    # Actions
    # Simple button actions

    def click_simple_button(self):
        self.get_simple_button_click().click()

    def assert_click_text(self):
        self.assert_values(self.get_click_text(),'Submitted')
        print('click done')




    # Disabled button klick actions

    def click_state(self):
        self.get_select_state().click()


    def click_disabled(self):
        self.get_disabled_status().click()


    def click_enabled(self):
        self.get_enabled_status().click()


    def click_submit_button(self):
        self.get_submit_button().click()


    def assert_submit_text(self):
        self.assert_values(self.get_submit_text(),'Submitted')
        print('click done')



