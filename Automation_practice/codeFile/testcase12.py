import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
# 4. Click on 'Products' button
driver.find_element(By.XPATH, "//a[text()=' Products']").click()

#5. Hover over first product and click 'Add to cart'
products_boxes = driver.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
first_product = products_boxes[0]
actions = ActionChains(driver)
actions.move_to_element(first_product).perform()
first_add_button = first_product.find_element(By.CSS_SELECTOR, ".add-to-cart")
first_add_button.click()
driver.find_element(By.CLASS_NAME, "btn btn-default add-to-cart").click()
second_product = products_boxes[1]
ActionChains(driver).move_to_element(second_product).perform()
second_product.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
driver.find_element(By.XPATH, "//u[text()='View Cart']").click()



time.sleep(5)
