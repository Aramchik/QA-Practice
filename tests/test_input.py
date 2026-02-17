import selenium
import pytest
from pages.input import InputPage
import allure


        # Test Inputs
# Test text input
@allure.feature('Inputs')
@allure.step('Text input')
def test_text_input(browser):
    with allure.step('Open browser, Text input page'):
        i = InputPage(browser)
        i.open_input_page()
    with allure.step('Typing text and assert input text'):
        i.typing_text_input()
        i.assert_text()




# Test Email field
@allure.feature('Inputs')
@allure.step('Email field')
def test_email_field_input(browser):
    with allure.step('Open browser, Email field page'):
        i = InputPage(browser)
        i.open_email_field_page()
    with allure.step('Typing email and assert input text'):
        i.typing_email_input()
        i.assert_email()



# Test Email field wrong email
@allure.feature('Inputs')
@allure.step('Email field error')
def test_email_field_input_error(browser):
    with allure.step('Open browser, Email field page'):
        i = InputPage(browser)
        i.open_email_field_page()
    with allure.step('Typing wrong email and assert input text'):
        i.typing_error_text_input_email()
        i.assert_error_email()


# Test Password field
@allure.feature('Inputs')
@allure.step('Email Password field ')
def test_password_field_input(browser):
    with allure.step('Open browser, Email field page'):
        i = InputPage(browser)
        i.open_password_field_page()
    with allure.step('Typing password and assert password'):
        i.typing_password_input()
        i.assert_password()


