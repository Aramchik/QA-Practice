import os
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import pytest
import allure



class BasePage:
    # initialization  browser
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)



    # function for assert
    def assert_values(self, word, result):
        value_word = word.text
        assert value_word == result



    # function for change window
    def switch_wwindow(self):
        self.browser.switch_to.window(self.browser.window_handles[1])



   # function for do screenshot
    def do_screenshot(self, name="screenshot"):
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")

        self.browser.save_screenshot(path)
        print(f"Скриншот: screenshots/{os.path.basename(path)}")

        allure.attach.file(
            path,
            name=f"{name} ({timestamp})",
            attachment_type=allure.attachment_type.PNG
        )

        return path




    # Function for give alert text
    def give_alert_text(self):
        alert = WebDriverWait(self.browser, 10).until(Ec.alert_is_present())
        alert_text = alert.text
        return alert_text




    # Function for accept alert
    def alert_accept(self):
        WebDriverWait(self.browser, 10).until(Ec.alert_is_present()).accept()
        print('Alert accepted')




    # Function for dismiss alert
    def alert_dismiss(self):
        WebDriverWait(self.browser, 10).until(Ec.alert_is_present()).dismiss()
        print('Alert dismiss')




    # Function for text in alert
    def text_alert(self):
        WebDriverWait(self.browser, 10).until(Ec.alert_is_present()).send_keys('Some text')



    # Function for get text
    def get_text(self, word):
        return word.text



    # Function for switch to iframe
    def switch_to_iframe(self):
        iframe = WebDriverWait(self.browser, 10).until(Ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
        print("Switch to iframe")


    # Function for switch back
    def switch_back_from_iframe(self):
        self.browser.switch_to.default_content()
        print("Switch to back")


    def refresh(self):
        self.browser.refresh()