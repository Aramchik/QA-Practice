import selenium
import pytest
from pages.text_area import TextArea
import allure


# Test textarea
@allure.feature('Text area')
@allure.step('Test text area')
def test_text_area(browser):
    with allure.step('Open browser, Text area page'):
        ta = TextArea(browser)
        ta.open_text_area_page()
    with allure.step('Typing text'):
        ta.typing_text()
    with allure.step('Do screenshot'):
        ta.do_screenshot()
    with allure.step('Click submit and assert'):
        ta.click_submit()
        ta.do_screenshot()
        ta.assert_text_area_input()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


    # Negative tests
# Click submit with null input
@allure.feature('Text area')
@allure.step('Negative test text area')
def test_text_area_negative(browser):
    with allure.step('Open browser, Text area page'):
        ta = TextArea(browser)
        ta.open_text_area_page()
    with allure.step('Click submit'):
        ta.click_submit()
    with allure.step('Do screenshot'):
        ta.do_screenshot()







# test only first chapter
@allure.feature('Multiply text area')
@allure.step('Test only first chapter')
def test_only_first(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in first chapter'):
        ta.typing_first_text()
    with allure.step('Click submit and assert'):
        ta.click_submit()
        ta.assert_first_text_area()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


# test first and second chapter
@allure.feature('Multiply text area')
@allure.step('Test first and second chapter')
def test_first_and_second(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in first chapter'):
        ta.typing_first_text()
    with allure.step('Typing text in second chapter'):
        ta.typing_second_text()
    with allure.step('Click submit and assert'):
        ta.click_submit()
        ta.assert_first_and_second_text_area()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


# test first second and third chapter
@allure.feature('Multiply text area')
@allure.step('Test first second and third chapter')
def test_first_second_third(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in first chapter'):
        ta.typing_first_text()
    with allure.step('Typing text in second chapter'):
        ta.typing_second_text()
    with allure.step('Typing text in third chapter'):
        ta.typing_third_text()
    with allure.step('Click submit and assert'):
        ta.click_submit()
        ta.assert_first_second_third_text_area()
    with allure.step('Do screenshot'):
        ta.do_screenshot()




# test first and third chapter
@allure.feature('Multiply text area')
@allure.step('Test first and third chapter')
def test_first_third(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in first chapter'):
        ta.typing_first_text()
    with allure.step('Typing text in third chapter'):
        ta.typing_third_text()
    with allure.step('Click submit and assert'):
        ta.click_submit()
        ta.assert_first_third_text_area()
    with allure.step('Do screenshot'):
        ta.do_screenshot()



    # Negative tests

# Test all null and click submit
@allure.feature('Negative tests Multiply text area')
@allure.step('Test all null and click submit')
def test_negative_all_null(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Click submit'):
        ta.click_submit()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


# Test first null, second not null and click submit
@allure.feature('Negative tests Multiply text area')
@allure.step('Test first null, second not null and click submit')
def test_negative_second(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in second chapter'):
        ta.typing_second_text()
    with allure.step('Click submit'):
        ta.click_submit()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


# Test first null, third not null and click submit
@allure.feature('Negative tests Multiply text area')
@allure.step('Test first null, third not null and click submit')
def test_negative_third(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in third chapter'):
        ta.typing_third_text()
    with allure.step('Click submit'):
        ta.click_submit()
    with allure.step('Do screenshot'):
        ta.do_screenshot()


# Test first null, second and third not null and click submit
@allure.feature('Negative tests Multiply text area')
@allure.step('Test first null, second and third not null and click submit')
def test_negative_second_and_third(browser):
    with allure.step('Open browser, Multiply text area'):
        ta = TextArea(browser)
        ta.open_multi_text_area_page()
    with allure.step('Typing text in second chapter'):
        ta.typing_second_text()
    with allure.step('Typing text in third chapter'):
        ta.typing_third_text()
    with allure.step('Click submit'):
        ta.click_submit()
    with allure.step('Do screenshot'):
        ta.do_screenshot()
