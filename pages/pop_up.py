from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage


# Lockators

launch_pop_up = (By.XPATH, '//*[@id="content"]/button')
close_button = (By.XPATH, '//div[@class="modal-footer"]/button[@class="btn btn-secondary"]')

# Modal lockators
select_me_or_not = (By.ID, 'id_checkbox_0')
send_button = (By.XPATH, '//div[@class="modal-footer"]/button[@class="btn btn-primary"]')

result_text = (By.ID, 'result-text')


# iframe pop-up lockators
text_for_copy = (By.XPATH, '//p[@id="text-to-copy"]')
check_button = (By.XPATH, '//div[@class="modal-footer"]/button[@class="btn btn-primary"]')

input_place = (By.XPATH, "//input[@type='text']")
submit_button = (By.ID, 'submit-id-submit')

iframe_result_text = (By.ID, 'check-result')





# Class for Pop-up page
class PopUp(BasePage):
    def __init__(self, browser):
        super().__init__(browser)






    # Open modal page
    def open_modal_page(self):
        self.browser.get("https://www.qa-practice.com/elements/popup/modal")



    # Open iframe pop up page
    def open_iframe_popup_page(self):
        self.browser.get("https://www.qa-practice.com/elements/popup/iframe_popup")







        # Getters

    # getters modal

    # getter Launch pop up
    def get_launch_pop_up(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(launch_pop_up))

    # getter select me or not
    def get_select_or_not(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(select_me_or_not))


    # getter close
    def get_close(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(close_button))


    # getter send
    def get_send(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(send_button))

    # getter result text
    def get_result_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(result_text))



    # Iframe pop up getters

    # getter text for copy
    def get_text_for_copy(self):
        return WebDriverWait(self.browser, 10).until(Ec.visibility_of_element_located(text_for_copy))


    # getter check button
    def get_check_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(check_button))


    # getter input place
    def get_input_place(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(input_place))


    # getter submit button
    def get_submit_button(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(submit_button))



    # getter iframe result text
    def get_iframe_result_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(iframe_result_text))








        # Actions

    # Modal actions

    # function click launch pop up
    def click_launch_pop_up(self):
        self.get_launch_pop_up().click()
        print('Click launch pop up')


    # function for click select me or not
    def click_select_me_or_not(self):
        self.get_select_or_not().click()
        print('You selected checkbox')



    # function for click send
    def click_send(self):
        self.get_send().click()
        print('You click send')


    # function for click close
    def click_close(self):
        self.get_close().click()
        print('You click close')



    # asert selected text if you click button select me or not
    def asert_selected_text(self):
        self.assert_values(self.get_result_text(),'select me or not')
        print('Text is good')



    # asert selected text without click button select me or not
    def asert_null_text(self):
        self.assert_values(self.get_result_text(),'None')
        print('You selected None')




    # Iframe actions

    # click Check button
    def click_check(self):
        self.get_check_button().click()
        print('Click Check button')


    # Click input place
    def click_input_place(self):
        self.get_input_place().click()
        print('Click input')



    # Send keys in Text from iframe
    def send_keys(self, text):
        self.get_input_place().send_keys(text)
        print('Typing text for copy')



    # Click submit
    def click_submit(self):
        self.get_submit_button().click()
        print('Click submit button')



    # Assert text for copy if copy
    def asert_copy_text(self):
        self.assert_values(self.get_iframe_result_text(),'Correct!')
        print('Text good')



    # Assert text for copy if send some text
    def asert_copy_text_some_text(self):
        self.assert_values(self.get_iframe_result_text(),'Nope. Better luck next time!')
        print('Text good')



    # All buisnes path. Click launch pop up, copy text, click check, send keys, click submit, and  asert text
    def all_buisnes_path(self):
        self.click_launch_pop_up()
        iframe = self.browser.find_element(By.TAG_NAME, 'iframe')
        self.browser.switch_to.frame(iframe)
        text_for_copy = self.browser.find_element(By.XPATH, '//p[@id="text-to-copy"]').text
        print(text_for_copy)
        self.browser.switch_to.default_content()
        self.click_check()
        self.send_keys(text_for_copy)
        self.click_submit()
        self.asert_copy_text()




    # All buisnes path, but aint copy text and send test keys and asert
    def all_buisnes_but(self):
        self.click_launch_pop_up()
        self.click_check()
        self.send_keys('some text')
        self.click_submit()
        self.asert_copy_text_some_text()
