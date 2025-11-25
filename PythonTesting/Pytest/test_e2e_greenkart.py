import json
import os
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

from pageObjects.Select_Veg import SelectVeg
from pageObjects.PlaceOrder import PlaceOrder
from pageObjects.Proceedorder import ProceedOrder

test_data_path = '../data/test_e2e_greenkart.json'
#/Users/anmolasati/PycharmProjects/PythonTesting/data/test_e2e_greenkart.json
with open( test_data_path ) as f:
    test_data = json.load( f )
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    selectVeg = SelectVeg(driver)
    selectVeg.add_to_cart(test_list_item["sabji"])
    selectVeg.proceed_to_cart()
    place_order = PlaceOrder(driver)
    place_order.validate_voucher(test_list_item["voucher"])
    place_order.verify_calculation()
    proceed_order = ProceedOrder(driver)
    proceed_order.confirmlocation(test_list_item["desh"])