from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserutils import BrowserUtils


class PlaceOrder(BrowserUtils):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.enter_code = (By.CLASS_NAME, "promoCode")
        self.verify_code = (By.CLASS_NAME, "promoBtn")
        self.wait_code = (By.CLASS_NAME, "promoInfo")
        self.message = (By.CLASS_NAME, "promoInfo")
        self.amount = (By.CSS_SELECTOR, "tr td:nth-child(5) p")
        self.totalamt = (By.CLASS_NAME, "totAmt")
        self.finalamt = (By.CLASS_NAME, "discountAmt")
        self.orderbtn = (By.XPATH, "//button[text()='Place Order']")


    def validate_voucher(self,voucher):
        self.driver.find_element(*self.enter_code).send_keys(voucher)
        self.driver.find_element(*self.verify_code).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((self.wait_code)))
        message = self.driver.find_element(*self.message).text
        print(message)
        assert message == "Code applied ..!"


    def verify_calculation(self):
        sum = 0
        amounts = self.driver.find_elements(*self.amount)
        for amount in amounts:
            sum = sum + int(amount.text)

        print(sum)
        totalamount = int(self.driver.find_element(*self.totalamt).text)
        assert totalamount == sum

        final = float(self.driver.find_element(*self.finalamt).text)

        assert final < totalamount

        self.driver.find_element(*self.orderbtn).click()
        proceedorder = ProceedOrder(self.driver)
        return proceedorder













