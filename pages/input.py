from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage

# Lockators
# text input
text_string = (By.XPATH, "//input[@name='text_string']")
text_input = (By.XPATH, "//p[@id='result-text']")

# email field
email_input = (By.XPATH, "//input[@name='email']")
email_text_input = (By.XPATH, "//p[@id='result-text']")
email_error_message = (By.XPATH, "//span[@id='error_1_id_email']")



# password field
password_input = (By.XPATH, "//input[@id='id_password']")
password_text_input = (By.XPATH, "//p[@id='result-text']")





# Class for Main page
class InputPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open input page
    def open_input_page(self):
        self.browser.get("https://www.qa-practice.com/elements/input/simple")



    # Open email field page
    def open_email_field_page(self):
        self.browser.get("https://www.qa-practice.com/elements/input/email")



    # Open password field page
    def open_password_field_page(self):
        self.browser.get("https://www.qa-practice.com/elements/input/passwd")





    # Getters
    # Text input getters
    def get_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(text_string))

    def get_text_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(text_input))



    def get_email_error_message(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(email_error_message))






    # email input getters
    def get_email_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(email_input))

    def get_text_email_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(email_text_input))




    # password input getters
    def get_password_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(password_input))

    def get_text_password_input(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(password_text_input))





    # Actions
    # Text input actions
    def typing_text_input(self):
        self.get_input().send_keys('text')
        self.get_input().send_keys(Keys.ENTER)


    def assert_text(self):
        self.assert_values(self.get_text_input(), "text")
        print('text is good')





    # email input actions
    def typing_email_input(self):
        self.get_email_input().send_keys('test@gmail.com')
        self.get_email_input().send_keys(Keys.ENTER)


    def typing_error_text_input_email(self):
        self.get_email_input().send_keys('test text')
        self.get_email_input().send_keys(Keys.ENTER)


    def assert_email(self):
        self.assert_values(self.get_text_email_input(), "test@gmail.com")
        print('email is good')


    def assert_error_email(self):
        self.assert_values(self.get_email_error_message(), "Enter a valid email address.")
        print('You typing wrong email')




    # password input actions
    def typing_password_input(self):
        self.get_password_input().click()
        self.get_password_input().send_keys('w5#7p9UF89uW')
        self.get_password_input().send_keys(Keys.ENTER)

    def assert_password(self):
        self.assert_values(self.get_text_password_input(), "w5#7p9UF89uW")
        print('password is good')