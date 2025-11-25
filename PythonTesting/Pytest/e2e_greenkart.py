import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword" ).send_keys("ber")
expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []

results = driver.find_elements(By.XPATH, "//div[@class='product']")
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert actuallist == expectedlist
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
(WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo"))))
message = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(message)
assert message == "Code applied ..!"

sum = 0

amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for amount in amounts:
    sum = sum + int(amount.text)

print(sum)
totalamount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert totalamount == sum

final = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert final < totalamount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
dropdown = Select(driver.find_element(By.XPATH, "//select[@style='width: 200px;']"))
dropdown.select_by_value("India")

driver.find_element(By.CLASS_NAME, "chkAgree").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()



time.sleep(2)
