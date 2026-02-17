
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage

# Lockators

submit_button = (By.XPATH, "//input[@id='submit-id-submit']")

# Single select lockators
chose_language = (By.XPATH, "//select[@id='id_choose_language']")

python_button = (By.XPATH, "//option[@value='1']")
ruby_button = (By.XPATH, "//option[@value='2']")
javascript_button = (By.XPATH, "//option[@value='3']")
java_button = (By.XPATH, "//option[@value='4']")
c_sharp_button = (By.XPATH, "//option[@value='5']")

select_text = (By.XPATH, "//p[@id='result-text']")


# Multiply select lockators
chose_place = (By.XPATH, "(//select)[1]")
sea_place = (By.XPATH, "(//select)[1]//option[@value='1']")
mountains_place = (By.XPATH, "(//select)[1]//option[@value='2']")
old_town_place = (By.XPATH, "(//select)[1]//option[@value='3']")
ocean_place = (By.XPATH, "(//select)[1]//option[@value='4']")
restaurant_place = (By.XPATH, "(//select)[1]//option[@value='2']")



# Choose how you want to get there*
chose_how = (By.XPATH, "(//select)[2]")

car_how = (By.XPATH, "(//select)[2]//option[@value='1']")
bus_how = (By.XPATH, "(//select)[2]//option[@value='2']")
train_how = (By.XPATH, "(//select)[2]//option[@value='3']")
air_how = (By.XPATH, "(//select)[2]//option[@value='4']")


# Choose when you want to go*
chose_when = (By.XPATH, "(//select)[3]")

today_when = (By.XPATH, "(//select)[3]//option[@value='1']")
tomorow_when = (By.XPATH, "(//select)[3]//option[@value='2']")
next_week_when = (By.XPATH, "(//select)[3]//option[@value='3']")









# Class for Slect page
class SelectPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)



    # Open simple select page
    def open_single_select_page(self):
        self.browser.get("https://www.qa-practice.com/elements/select/single_select")


    # Open multi select page
    def open_mult_select_page(self):
        self.browser.get("https://www.qa-practice.com/elements/select/mult_select")






    # Getters
    # Single select getters

    def get_chose_language(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(chose_language))

    def get_python(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(python_button))

    def get_ruby(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(ruby_button))

    def get_js(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(javascript_button))

    def get_java(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(java_button))

    def get_c_sharp(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(c_sharp_button))


    def get_submit(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(submit_button))


    def get_selected_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(select_text))





    # Getters
    # Multi select getters

    # Select place
    def get_chose_place(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(chose_place))


    # Select acurate place
    def get_sea(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(sea_place))

    def get_mountains(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(mountains_place))

    def get_old_town(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(old_town_place))

    def get_ocean(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(ocean_place))

    def get_restaurant(self):
        return WebDriverWait(self.browser,10).until(Ec.element_to_be_clickable(restaurant_place))



    # Select how
    def get_chose_how(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(chose_how))



    # Select acurate how
    def get_car(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(car_how))

    def get_bus(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(bus_how))

    def get_train(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(train_how))

    def get_air(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(air_how))





    # Select when
    def get_chose_when(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(chose_when))

    # Select  acurate when

    def get_today_when(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(today_when))

    def get_tomorrow_when(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(tomorow_when))

    def get_next_week_when(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(next_week_when))








    # Actions
    # Single select actions

    def click_chose(self):
        self.get_chose_language().click()


    def click_puthon(self):
        self.get_python().click()

    def click_ruby(self):
        self.get_ruby().click()

    def click_js(self):
        self.get_js().click()


    def click_java(self):
        self.get_java().click()


    def click_c_sharp(self):
        self.get_c_sharp().click()


    def click_submit(self):
        self.get_submit().click()
        print('Click submit button')




    # Multi select actions

    # Place select actions
    def click_chose_place(self):
        self.get_chose_place().click()
        print('Click chose place')


    def click_sea(self):
        self.get_sea().click()
        print('Click sea')



    def click_mountains(self):
        self.get_mountains().click()
        print('Click mountains')


    def click_old_town(self):
        self.get_old_town().click()
        print('Click old town')


    def click_ocean(self):
        self.get_ocean().click()
        print('Click ocean')


    def click_restaurant(self):
        self.get_restaurant().click()
        print('Click restaurant')






    # How select actions

    def click_chose_how(self):
        self.get_chose_how().click()
        print('Click chose how')


    def click_car(self):
        self.get_car().click()
        print('Click car')


    def click_bus(self):
        self.get_bus().click()
        print('Click bus')


    def click_train(self):
        self.get_train().click()
        print('Click train')


    def click_air(self):
        self.get_air().click()
        print('Click air')




    # When select actions

    def click_chose_when(self):
        self.get_chose_when().click()
        print('Click chose when')



    def click_today_when(self):
        self.get_today_when().click()
        print('Click today when')


    def click_tomorrow_when(self):
        self.get_tomorrow_when().click()
        print('Click tomorrow when')


    def click_next_week_when(self):
        self.get_next_week_when().click()
        print('Click next week when')













    # assert single select texts

    def assert_python(self):
        self.assert_values(self.get_selected_text(), "Python")
        print('You selected Python')


    def assert_ruby(self):
        self.assert_values(self.get_selected_text(), "Ruby")
        print('You selected Ruby')


    def assert_js(self):
        self.assert_values(self.get_selected_text(), "JavaScript")
        print('You selected JavaScript')


    def assert_java(self):
        self.assert_values(self.get_selected_text(), "Java")
        print('You selected Java')


    def assert_c_sharp(self):
        self.assert_values(self.get_selected_text(), "C#")
        print('You selected C#')




    # assert multi select texts

    # if chose sea car today
    def assert_sea_car_today(self):
        self.assert_values(self.get_selected_text(),"to go by car to the sea today")
        print('You selected to go by car to the sea today')




    def negative_test(self):
        self.click_submit()
        required_selects = self.browser.find_elements(By.CSS_SELECTOR, "select[required]")
        first_required_select = required_selects[0]
        WebDriverWait(self.browser, 5).until(lambda d: first_required_select.get_attribute("validationMessage") != "")
        error_msg = first_required_select.get_attribute("validationMessage")
        print("Сообщение валидации:", error_msg)
