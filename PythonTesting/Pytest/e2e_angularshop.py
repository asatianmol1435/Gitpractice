from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"nav-link").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH,"div/h4")
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR, "a[text()*='Checkout']").click()
driver.find_element(By.CLASS_NAME,"btn btn-success").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,"India"))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.ID,"checkbox2").click()
driver.find_element(By.CLASS_NAME,"btn btn-success btn-lg").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in message
