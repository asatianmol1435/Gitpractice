import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

#service_object = Service("chromedriver")
#driver = webdriver.Chrome(service=service_object)

driver = webdriver.Chrome()

#Angular page
#driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.maximize_window()
#driver.find_element(By.NAME, "name").send_keys("Anmol")
#driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
#driver.find_element(By.ID, "exampleInputPassword1").send_keys(123456)
#driver.find_element(By.ID, "exampleCheck1").click()
#dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
#driver.find_element(By.ID, "inlineRadio1").click()
#driver.find_element(By.CLASS_NAME, "btn-success").click()
#message = driver.find_element(By.CLASS_NAME, "alert-success").text
#print(message)

#assert "Success" in message

#Forgot password page

#driver.get("http://www.rahulshettyacademy.com/client")
#driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
#driver.find_element(By.XPATH, "//input[@type='email']").send_keys("hello@gmail.com")
#driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")
#driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("123456")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Handling static dropdown
#driver.get("https://rahulshettyacademy.com/angularpractice/")
#dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)

# Handling dynamic dropdown

#driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#driver.find_element(By.ID, "autosuggest").send_keys("ind")
#time.sleep(2)
#countries = driver.find_elements(By.CLASS_NAME, "ui-corner-all")

# noinspection PyTypeChecker
#for country in countries:
#    if country.text == "India":
#        country.click()
#        break

#print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))


## selecting checkbox

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#checkboxes = driver.find_elements(By.XPATH, "//input[@id='checkBoxOption2']")

#for checkbox in checkboxes:
#    if checkbox.get_attribute("value") == "option2":
#       checkbox.click()
#        assert checkbox.is_selected()
#        break

## selecting checkbox

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#radios = driver.find_elements(By.XPATH, "//input[@value='radio2']")

#for radio in radios:
#    if radio.get_attribute("value") == "radio2":
#        radio.click()
#        assert radio.is_selected()
#        break

#driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#name = "Anmol"
#driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
#driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
#alert = driver.switch_to.alert
#alerttext = alert.text
#print(alerttext)
#assert name in alerttext
#alert.accept()
#alert.dismiss()

#name = "Anmol"
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)

#driver.find_element(By.XPATH, "//input[@class='btn-style']").click()

#alert = driver.switch_to.alert

#alerttext1 = alert.text
#print(alerttext1)
#assert name in alerttext1
#alert.accept()

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("berry")
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(results)
print(len(results))
assert count >0

for result in results:
    result.find_element(By.XPATH, ".//button").click() # No need to add Xpath in its format here, because this line is searching for button inside line 117

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[@type='button']").click()
#Sum validation
Prices = driver.find_element(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in Prices:
    sum = sum + int(price.text)

print(sum)
totalamount = driver.find_element(By.CSS_SELECTOR, ".totAmt")

assert sum == int(totalamount)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

prices = driver.find_element(By.CSS_SELECTOR, "tr td:n-thchild(5) p")


















time.sleep(3)
