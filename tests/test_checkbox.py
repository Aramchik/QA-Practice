import selenium
import pytest
from pages.checkbox import CheckboxPage
import allure
import time 

    # Tests Single checkbox page
# test click submit without checkbox
@allure.feature('Single Checkbox')
@allure.step('Click submit without checkbox')
def test_click_submit(browser):
    with allure.step('Open Checkbox page, Single checkbox page'):
        cp = CheckboxPage(browser)
        cp.open_simple_checkbox_page()
    with allure.step('Click submit button'):
        cp.click_submit_button()



# test click submit with checkbox
@allure.feature('Single Checkbox')
@allure.step('Click submit with checkbox')
def test_single_checkbox(browser):
    with allure.step('Open Checkbox page, Single checkbox page'):
        cp = CheckboxPage(browser)
        cp.open_simple_checkbox_page()
    with allure.step('Click submit button'):
        cp.click_select_checkbox()
        cp.click_submit_button()
    with allure.step('Asert selected text'):
        cp.assert_selected_text()





# Test Checkboxes page

# test click submit without checkbox
@allure.feature('Checkboxes')
@allure.step('Click submit without checkbox')
def test_click_submit_2(browser):
    with allure.step('Open Checkbox page, Checkboxes page'):
        cp = CheckboxPage(browser)
        cp.open_checkboxs_page()
    with allure.step('Click submit button'):
        cp.click_submit_button()
        print('Click submit button')



# test click submit with checkbox 1 2 3
@allure.feature('Checkboxes')
@allure.step('Click submit with 1 2 3 checkbox')
def test_click_chekboxs(browser):
    with allure.step('Open Checkbox page, Checkboxes page'):
        cp = CheckboxPage(browser)
        cp.open_checkboxs_page()
        cp.do_screenshot()
    with allure.step('Click 1 checkbox'):
        cp.only_one()
        do_screenshot
        time.sleep(2)
    with allure.step('Click 2 checkbox'):
        cp.only_two()
        do_screenshot
        time.sleep(2)
    with allure.step('Click 3 checkbox'):
        cp.only_three()
        do_screenshot
        time.sleep(2)
    with allure.step('Click 1 and 2 checkboxes'):
        cp.one_two()
        do_screenshot
        time.sleep(2)
    with allure.step('Click 1 and 3 checkboxes'):
        cp.one_three()
        do_screenshot
        time.sleep(2)
    with allure.step('Click 2 and 3 checkboxes'):
        cp.two_three()
    with allure.step('Click 1 2 3 checkboxes'):
        cp.all()
        do_screenshot

