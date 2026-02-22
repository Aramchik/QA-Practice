import selenium
import pytest
from pages.select import SelectPage
import allure
import time


    # Select
# test single select
@allure.feature('Single Select')
def test_single_select(browser):
    with allure.step('Open browser, Single select page'):
        sp = SelectPage(browser)
        sp.open_single_select_page()

    # Test python
    with allure.step('Chose python, click submit and assert'):
        sp.click_chose()
        sp.do_screenshot()
        sp.click_puthon()
        sp.click_submit()
        sp.assert_python()

    time.sleep(1)
    
    # Test Ruby
    with allure.step('Chose ruby, click submit and assert'):
        sp.click_chose()
        sp.click_ruby()
        sp.click_submit()
        sp.assert_ruby()

    time.sleep(1)
    
    # Test JS
    with allure.step('Chose JS, click submit and assert'):
        sp.click_chose()
        sp.click_js()
        sp.click_submit()
        sp.assert_js()

    time.sleep(1)

    
    # Test Java
    with allure.step('Chose Java, click submit and assert'):
        sp.click_chose()
        sp.do_screenshot()
        sp.click_java()
        sp.do_screenshot()
        sp.click_submit()
        sp.do_screenshot()
        sp.assert_java()
        


    time.sleep(1)

    # Test C#
    with allure.step('Chose C#, click submit and assert'):
        sp.click_chose()
        sp.click_c_sharp()
        sp.click_submit()
        sp.assert_c_sharp()

    time.sleep(1)

# Test multi select
@allure.feature('Multi selects')
def test_multi_select(browser):
    with allure.step('Open browser, Multie selects page'):
        sp = SelectPage(browser)
        sp.open_mult_select_page()

    with allure.step('Chose place sea'):
        sp.click_chose_place()
        sp.click_sea()

    with allure.step('Chose how car'):
        sp.click_chose_how()
        sp.click_car()

    with allure.step('Chose when today'):
        sp.click_chose_when()
        sp.click_today_when()

    with allure.step('Click submit and assert result'):
        sp.click_submit()
        sp.assert_sea_car_today()




# Negative test
@allure.feature('Multi selects')
@allure.step('Negative test')
def test_negative_test(browser):
    with allure.step('Open browser, Multie selects page'):
        sp = SelectPage(browser)
        sp.open_mult_select_page()
    with allure.step('Click submit and wait warning message'):
        sp.negative_test()
    with allure.step('Do Screenshot'):
        sp.do_screenshot()

