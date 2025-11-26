from selenium.webdriver.common.by import By

from Utils.browserUtils import BrowserUtils


class Cart_page(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.cart_page = (By.XPATH, "//a[text()=' Cart']")
        self.subscription_text = (By.XPATH,"//h2[text()='Subscription']")
        self.subscription_email = (By.ID,"susbscribe_email")
        self.arrow_button = (By.ID,"subscribe")
        self.subscribe_text = (By.XPATH,"//*[contains(text(),'You have been successfully subscribed!')]")



    def subscription_page(self,email):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        subscription_text = self.driver.find_element(*self.subscription_text).text
        assert subscription_text == "SUBSCRIPTION"
        self.driver.find_element(*self.subscription_email).send_keys(email)
        self.driver.find_element(*self.arrow_button).click()
        subscribe_text = self.driver.find_element(*self.subscribe_text).text
        assert subscribe_text == "You have been successfully subscribed!"



