import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utils.browserUtils import BrowserUtils


class Delete_Account(BrowserUtils):

    def __init__(self, driver):
        self.driver = driver
        self.delete_button = (By.XPATH, "//a[text() = ' Delete Account']")
        self.delete_confirmation_text = (By.XPATH, "//*[text()='Account Deleted!']")
        self.delete_continue_button = (By.XPATH, "//a[@data-qa = 'continue-button']")


    def delete_account_and_confirmation(self):

        # 17. Click 'Delete Account' button
        self.driver.find_element(*self.delete_button).click()

        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        delete_text = self.driver.find_element(*self.delete_confirmation_text).text
        assert delete_text == "ACCOUNT DELETED!"
        self.driver.find_element(*self.delete_continue_button).click()





