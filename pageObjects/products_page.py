from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Utils.browserUtils import BrowserUtils


class Products_page(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.products_button = (By.XPATH, "//a[text()=' Products']")
        self.all_products_text = (By.XPATH,"//h2[@class='title text-center']")
        self.first_view_products_button = (By.XPATH, "//a[contains(text(),'View Product')][1]")
        self.product_name = (By.XPATH,"//div[@class='product-information']/h2")
        self.product_category = (By.XPATH,"//p[contains(text(),'Category')]")
        self.product_price = (By.XPATH,"//span[contains(text(),'Rs.')]")
        self.product_availability = (By.XPATH, "//b[contains(text(),'Avail')]")
        self.product_condition = (By.XPATH, "//b[contains(text(),'Condition')]")
        self.product_brand = (By.XPATH, "//b[contains(text(),'Brand')]")
        self.search_product = (By.ID, "search_product")
        self.search_click = (By.ID, "submit_search")
        self.verify_searched_products = (By.XPATH,"//h2[text()='Searched Products']")
        self.all_searched_products = (By.XPATH,"//div[@class='productinfo text-center']")


    def verify_products_page(self):
        #4. Click on 'Products' button
        self.driver.find_element(*self.products_button).click()

        #5. Verify user is navigated to ALL PRODUCTS page successfully
        expected_url = "https://automationexercise.com/products"
        assert expected_url == self.driver.current_url

        #6. The products list is visible
        all_products_text = self.driver.find_element(*self.all_products_text).text
        assert "ALL" in all_products_text

    def click_first_products_button(self):
        # 7. Click on 'View Product' of first product
        self.driver.find_element(*self.first_view_products_button).click()

        #8. User is landed to product detail page
        expected_product_url = "https://automationexercise.com/product_details/1"
        assert expected_product_url == self.driver.current_url

        #9. Verify that detail is visible: product name, category, price, availability, condition, brand

        name = self.driver.find_element(*self.product_name).text
        assert name != ""
        category = self.driver.find_element(*self.product_category).text
        assert "Category:" in category
        price = self.driver.find_element(*self.product_price).text
        assert "Rs." in price
        availability = self.driver.find_element(*self.product_availability).text
        assert "Availability:" in availability
        condition = self.driver.find_element(*self.product_condition).text
        assert "Condition:" in condition
        brand = self.driver.find_element(*self.product_brand).text
        assert "Brand:" in brand

    def search_products(self,search_product):
        # 4. Click on 'Products' button
        self.driver.find_element(*self.products_button).click()

        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        expected_url = "https://automationexercise.com/products"
        assert expected_url == self.driver.current_url

        #6. Enter product name in search input and click search button

        self.driver.find_element(*self.search_product).send_keys(search_product)
        self.driver.find_element(*self.search_click).click()
        searched_products_text = self.driver.find_element(*self.verify_searched_products).text
        assert searched_products_text == "SEARCHED PRODUCTS"
        products = self.driver.find_elements(*self.all_searched_products)
        assert len(products) >0
        for p in products:
            assert p.is_displayed()







