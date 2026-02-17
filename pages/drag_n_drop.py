from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from pages.base import BasePage


# Lockators
# Boxes
drop_here = (By.ID, "rect-droppable")
drag_me = (By.ID, 'rect-draggable')

result_drop = (By.ID, 'text-droppable')

# images lockators
drop_here_2 = (By.ID, "rect-droppable2")
drag_me_image = (By.XPATH, '//div[@id="rect-droppable1"]//img')

result_drop_2 = (By.XPATH, "(//p[@class='text-droppable'])[2]")





# Class for Drag-N-Drop page
class DragNDrop(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Open boxes page
    def open_boxes_page(self):
        self.browser.get("https://www.qa-practice.com/elements/dragndrop/boxes")



    # Open images page
    def open_images_page(self):
        self.browser.get("https://www.qa-practice.com/elements/dragndrop/images")







        # Getters

    # getters boxes
    # getter drop here
    def get_drop_here(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(drop_here))


    # getter drag me
    def get_drag_me(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(drag_me))



    # getter result text droped
    def get_droped_text(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(result_drop))







    # Getter images lockators
    # get drop here 2
    def get_drop_here_2(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(drop_here_2))



    # getter drag me image
    def get_drag_me_image(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(drag_me_image))


    # getter droped text image
    def get_droped_text_2(self):
        return WebDriverWait(self.browser, 10).until(Ec.element_to_be_clickable(result_drop_2))






        # Actions
    # Boxes actions
    def click_and_move(self):
        self.actions.drag_and_drop(self.get_drag_me(),self.get_drop_here()).perform()


    # Images actions
    def click_and_move_2(self):
        self.actions.drag_and_drop(self.get_drag_me_image(),self.get_drop_here_2()).perform()











        # Asserts
    # Boxes asserts
    def assert_droped_text(self):
        self.assert_values(self.get_droped_text(),'Dropped!')
        print('Drag n drop done')


    # Images asserts
    def assert_droped_text_2(self):
        self.assert_values(self.get_droped_text_2(),'Dropped!')
        print('Drag n drop done')