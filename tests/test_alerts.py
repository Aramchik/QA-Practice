import selenium
import pytest
from pages.alerts import Alerts
import allure


    # Test Alerts

# Test alert box
@allure.feature('Alert box')
def test_alerts(browser):
    with allure.step('Open browser'):
        al = Alerts(browser)
        al.open_alert_box_page()
    with allure.step('Click button click and check alert'):
        al.click_1()
        print(al.give_alert_text())
        assert al.give_alert_text() == 'I am an alert!'
        print('alert text is good')
        al.alert_accept()



    # Test alert Confirmation box

# Test click ok
@allure.feature('Alert Confirmation box')
def test_click_ok(browser):
    with allure.step('Open browser'):
        al = Alerts(browser)
        al.open_confirmation_box_page()

    with allure.step('Click click button'):
        al.click_2()
    print(al.give_alert_text())

    with allure.step('Assert alert text'):
        assert al.give_alert_text() == 'Select Ok or Cancel'
        print('alert text is good')

    with allure.step('Click ok'):
        al.alert_accept()
        al.assert_result_text_ok()



    # Test click cancel
    with allure.step('Refresh browser'):
        al.refresh()

    with allure.step('Open browser'):
        al.click_2()
    print(al.give_alert_text())

    with allure.step('Assert alert text'):
        assert al.give_alert_text() == 'Select Ok or Cancel'
        print('alert text is good')

    with allure.step('Click cancel'):
        al.alert_dismiss()
        al.assert_result_text_cancel()





        # Test Promt box
# Test text something in alert
@allure.feature('Promt box')
def test_text_alert(browser):
    with allure.step('Open browser'):
        al = Alerts(browser)
        al.open_alert_promt_box_page()

    with allure.step('Click click button'):
        al.click_3()

    print(al.give_alert_text())

    with allure.step('Assert alert text'):
        assert al.give_alert_text() == 'Please enter some text'
        print('alert text is good')
    with allure.step('Typing some text and click ok'):
        al.text_alert()
        al.alert_accept()
        al.assert_result_text_typing()