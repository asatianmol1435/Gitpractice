from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utils.browserutils import BrowserUtils


class ProceedOrder(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.select_country = (By.XPATH, "//select[@style='width: 200px;']")
        self.checkbox = (By.CLASS_NAME, "chkAgree")
        self.proceedbtn = (By.XPATH, "//button[text()='Proceed']")


    def confirmlocation(self,desh):
        dropdown = Select(self.driver.find_element(*self.select_country))
        dropdown.select_by_value(desh)
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.proceedbtn).click()

