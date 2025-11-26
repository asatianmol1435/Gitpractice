from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserUtils import BrowserUtils


class Testcase_page(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.testcase_button = (By.XPATH, "//a[text()=' Test Cases']")

    def test_case_page(self):
        #4. Click on 'Test Cases' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.testcase_button))
        self.driver.find_element(*self.testcase_button).click()

        #5. Verify user is navigated to test cases page successfully
        expected_url = "https://automationexercise.com/test_cases"
        assert expected_url == self.driver.current_url