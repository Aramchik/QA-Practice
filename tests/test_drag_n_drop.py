import selenium
import pytest
from pages.drag_n_drop import DragNDrop
import allure


    # Test Drag n drop
# Test boxes
@allure.feature('Drag n drop')
@allure.step('Test Boxes')
def test_boxes(browser):
    with allure.step('Open browser, Boxes page'):
        dd = DragNDrop(browser)
        dd.open_boxes_page()
    with allure.step('Click and move, assert droped text'):
        dd.click_and_move()
        dd.assert_droped_text()


# Test images
@allure.feature('Drag n drop')
@allure.step('Test Images')
def test_images(browser):
    with allure.step('Open browser, Boxes page'):
        dd = DragNDrop(browser)
        dd.open_images_page()
    with allure.step('Click and move, assert droped text'):
        dd.click_and_move_2()
        dd.assert_droped_text_2()