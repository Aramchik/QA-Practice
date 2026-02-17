import allure
import selenium
import pytest
from pages.pop_up import PopUp


            # Test Pop-up
    # Modal tests

# Test click button send with checkbox select me or not
@allure.feature('Pop-up Modal')
@allure.step('Click button with checkbox')
def test_select_me(browser):
    with allure.step('Open browser, Pop-up Modal page'):
        pu = PopUp(browser)
        pu.open_modal_page()
    with allure.step('Click launch Pop-up'):
        pu.click_launch_pop_up()
    with allure.step('Click checkbox select me or not'):
        pu.click_select_me_or_not()
    with allure.step('Click send and assert'):
        pu.click_send()
        pu.asert_selected_text()


# Test click button send without checkbox select me or not
@allure.feature('Pop-up Modal')
@allure.step('Click button without checkbox')
def test_not_select(browser):
    with allure.step('Open browser, Pop-up Modal page'):
        pu = PopUp(browser)
        pu.open_modal_page()
    with allure.step('Click launch Pop-up'):
        pu.click_launch_pop_up()
    with allure.step('Click send and assert'):
        pu.click_send()
        pu.asert_null_text()


# Test click close button with checkbox select me or not
@allure.feature('Pop-up Modal')
@allure.step('Click close button with checkbox')
def test_close_select(browser):
    with allure.step('Open browser, Pop-up Modal page'):
        pu = PopUp(browser)
        pu.open_modal_page()
    with allure.step('Click launch Pop-up'):
        pu.click_launch_pop_up()
    with allure.step('Click checkbox select me or not'):
        pu.click_select_me_or_not()
    with allure.step('Click close'):
        pu.click_close()


# Test click close button without checkbox select me or not
@allure.feature('Pop-up Modal')
@allure.step('Click close button without checkbox')
def test_close(browser):
    with allure.step('Open browser, Pop-up Modal page'):
        pu = PopUp(browser)
        pu.open_modal_page()
    with allure.step('Click launch Pop-up'):
        pu.click_launch_pop_up()
    with allure.step('Click close'):
        pu.click_close()






    # Test iframe Pop-up
# Test click Launch Pop-up copy and check
@allure.feature('Iframe Pop-up')
@allure.step('Click Launch Pop-up copy and check')
def test_copy_and_check(browser):
    with allure.step('Open browser, Iframe Pop-up page'):
        pu = PopUp(browser)
        pu.open_iframe_popup_page()
    with allure.step('Click Launch Pop-up, copy, check, past, submit and assert'):
        pu.all_buisnes_path()


# Test click Launch Pop-up and check
@allure.feature('Iframe Pop-up')
@allure.step('Click Launch Pop-up and check')
def test_check(browser):
    with allure.step('Open browser, Iframe Pop-up page'):
        pu = PopUp(browser)
        pu.open_iframe_popup_page()
    with allure.step('Click Launch Pop-up, check, past some text, submit and assert'):
        pu.all_buisnes_but()


# Test click Launch Pop-up and close
@allure.feature('Iframe Pop-up')
@allure.step('Click Launch Pop-up and close')
def test_check_close(browser):
    with allure.step('Open browser, Iframe Pop-up page'):
        pu = PopUp(browser)
        pu.open_iframe_popup_page()
    with allure.step('Click Launch Pop-up'):
        pu.click_launch_pop_up()
    with allure.step('Click close'):
        pu.click_close()