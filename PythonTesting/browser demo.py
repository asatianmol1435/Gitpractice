import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

#service_object = Service("chromedriver")
#driver = webdriver.Chrome(service=service_object)

driver = webdriver.Chrome()

driver.get("http://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value("")

# XPATH - "//tagname[@attribute='value']" -> "//input[@type='submit']"
# XPATH, if multiple tag are same - ("//tagname[@attribute='value']) [3]" -> "(//input[@type='submit']) [3]"
# CSS - "tagname[attribute='value']" -> "input[type='submit']" #id, .classname
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message # Pass

driver.find_element(By.XPATH, "(//input[@type='text']) [3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text']) [3]").clear()


time.sleep(2)