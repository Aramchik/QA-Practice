import selenium
import pytest
from pages.button import ButtonPage
import allure

    # Test Simple Button
@allure.feature('Buttons')
@allure.step('Simple button')
def test_simple_button(browser):
    with allure.step('Open browser, Simple page'):
        bp = ButtonPage(browser)
        bp.open_simple_button_page()
    with allure.step('Click click button'):
        bp.click_simple_button()
        print('Click simple button')
    with allure.step('Assert text after click'):
        bp.assert_click_text()


    # Test Disabled Button
@allure.feature('Buttons')
@allure.step('Disabled button')
def test_disabled_button(browser):
    with allure.step('Open browser, Disabled page'):
        bp = ButtonPage(browser)
        bp.open_disabled_button_page()
    with allure.step('Try click Submit button, after change enabled and try again'):
        try:
            bp.click_submit_button()
        except:
            bp.click_state()
            bp.click_enabled()
            bp.click_submit_button()
        bp.assert_submit_text()