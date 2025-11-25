from selenium.webdriver.common.by import By

from Utils.browserutils import BrowserUtils
from pageObjects.PlaceOrder import PlaceOrder


class SelectVeg(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.searchveg = (By.CSS_SELECTOR, ".search-keyword")
        self.cart_button = (By.XPATH, "//img[@alt='Cart']")
        self.proceed = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")


    def add_to_cart(self,sabji):
        expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        actuallist = []
        self.driver.find_element(*self.searchveg).send_keys(sabji)
        results = self.driver.find_elements(By.XPATH, "//div[@class='product']")
        for result in results:
            actuallist.append(result.find_element(By.XPATH, "h4").text)
            result.find_element(By.XPATH, "div/button").click()
        #assert(actuallist == expectedlist)


    def proceed_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.proceed).click()
        placeorder = PlaceOrder(self.driver)
        return placeorder