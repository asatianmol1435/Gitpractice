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
from pageObjects.login import Login_page
from pageObjects.signup import SignUp
#sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )
test_data_path = '/Users/anmolasati/PycharmProjects/git/Automation_practice/Data/test_testcase2.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance,test_list_item):
    driver = browser_instance
    driver.get('https://automationexercise.com')
    login = Login_page(driver)
    login.login(test_list_item["login_email"], test_list_item["login_password"])
    signup = SignUp(driver)
    signup.verify_logged_in_page()
    #delete_account = Delete_Account(driver)
    #delete_account.delete_account_and_confirmation()

    # runs perfectly unless ads
    #Test Case 2: Login User with correct email and password













