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

from pageObjects.delete_account_page import Delete_Account
from pageObjects.signup import SignUp
#sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
test_data_path = '/Users/anmolasati/PycharmProjects/git/Automation_practice/Data/test_testcase1.json'
#/Users/anmolasati/PycharmProjects/PythonTesting/data/test_e2e_greenkart.json
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance,test_list_item):
    driver = browser_instance
    driver.get('https://automationexercise.com')
    signup = SignUp(driver)
    signup.signup_page(test_list_item["name"], test_list_item["email"])
    signup.signup_information_page(
        test_list_item["password"],
        test_list_item["first_name"],
        test_list_item["last_name"],
        test_list_item["company"],
        test_list_item["address1"],
        test_list_item["address2"],
        test_list_item["state"],
        test_list_item["city"],
        test_list_item["zipcode"],
        test_list_item["mobile_num"]
    )
    signup.signup_confirmation_page()
    signup.verify_logged_in_page()
    #delete_account = Delete_Account(driver)
    #delete_account.delete_account_and_confirmation()

    # runs perfectly unless ads
    #Test Case 1: Register User













