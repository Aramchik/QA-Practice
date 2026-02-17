import selenium
import pytest
from pages.new_tab import NewTabPage
import allure


        # Tests New tab
# test new tab link
@allure.feature('New tab')
@allure.step('Test New tab link')
def test_new_tab_link(browser):
    with allure.step('Open browser, New tab link page'):
        nt = NewTabPage(browser)
        nt.open_new_tab_link_page()
    with allure.step('Click link'):
        nt.click_link()
    with allure.step('Switch window and assert result text'):
        nt.switch_wwindow()
        nt.assert_result_text()



# test new tab button
@allure.feature('New tab')
@allure.step('Test New tab button')
def test_new_tab_button(browser):
    with allure.step('Open browser, New tab button page'):
        nt = NewTabPage(browser)
        nt.open_new_tab_button_page()
    with allure.step('Click button'):
        nt.click_click_button()
    with allure.step('Switch window and assert result text'):
        nt.switch_wwindow()
        nt.assert_result_text()