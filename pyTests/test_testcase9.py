import json
import os
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.contact_us_page import Contact_us_page
from pageObjects.delete_account_page import Delete_Account
from pageObjects.products_page import Products_page
from pageObjects.signup import SignUp
from pageObjects.testcase_page import Testcase_page

#sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
test_data_path = '/Users/anmolasati/PycharmProjects/git/Automation_practice/Data/test_testcase9.json'
#/Users/anmolasati/PycharmProjects/PythonTesting/data/test_e2e_greenkart.json
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance,test_list_item):
    driver = browser_instance
    driver.get('https://automationexercise.com')
    products_page = Products_page(driver)
    products_page.search_products(test_list_item["search_product"])

    # runs perfectly unless ads
    #Test Case 9: Search Product






