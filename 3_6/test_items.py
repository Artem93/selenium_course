import pytest
from selenium import webdriver
import time


def test_item_has_add_to_cart_button(browser: webdriver.Chrome):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    count_basket_btn = browser.find_elements_by_class_name("btn-add-to-basket").__len__()
    assert count_basket_btn == 1, f"Expected 1 basket button, got {count_basket_btn}"
