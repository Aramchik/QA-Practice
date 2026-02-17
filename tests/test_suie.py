import selenium
import pytest
from pages.main import MainPage
import allure


        # Test drop down in home page
@allure.feature('Drop down in home page')
def test_click_drop_down(browser):
    with allure.step('Open home page'):
        m = MainPage(browser)
        m.open_main_page()
    with allure.step('Click drop down'):
        m.click_suie()