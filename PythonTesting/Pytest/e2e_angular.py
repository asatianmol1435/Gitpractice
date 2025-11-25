import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Anmol")
driver.find_element(By.NAME,"email").send_keys("anmolasati22@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Hello@12345")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element(By.XPATH, "//input[@value='option1']").click()
driver.find_element(By.NAME, "bday").send_keys("20/06/1999")
driver.find_element(By.CLASS_NAME, "btn-success").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success!" in message

time.sleep(2)


