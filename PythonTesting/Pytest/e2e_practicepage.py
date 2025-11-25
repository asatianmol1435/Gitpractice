import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option1")
dropdown.select_by_index(2)

#radio button
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

#checkbox
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break

#Java alert - Alert +Confirm(Ok & cancel both)
driver.find_element(By.ID, "name").send_keys("Anmol")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert "Anmol" in alerttext
alert.accept()
driver.switch_to.default_content()
driver.find_element(By.ID, "name").send_keys("Anmol")
driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert "Anmol" in alerttext
alert.dismiss()
driver.switch_to.default_content()
driver.find_element(By.ID, "name").send_keys("Anmol")
driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert "Anmol" in alerttext
alert.accept()
driver.switch_to.default_content()

#Mouse hover
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
#actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

#Handling new windows
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
grabtext = driver.find_element(By.TAG_NAME, "h3").text
print(grabtext)
driver.switch_to.window(windows[0])
grabtext1 = driver.find_element(By.TAG_NAME, "h3").text
print(grabtext1)

#handling frames
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"//a[text()='Blog']").click()
driver.find_element(By.CLASS_NAME, "tcb-button-text").click()
driver.switch_to.default_content()













time.sleep(5)



