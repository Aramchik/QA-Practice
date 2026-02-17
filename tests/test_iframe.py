import allure
import selenium
import pytest
from pages.iframe import Iframe



    # Test Iframe
# test click navbar in iframe
@allure.feature('Iframe')
def test_iframe(browser):
    with allure.step('Open browser, iframe page'):
        ifr = Iframe(browser)
        ifr.open_iframe_page()
    with allure.step('Switch to iframe'):
        ifr.switch_to_iframe()
    with allure.step('Click navbar'):
        ifr.click_navbar()