from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserUtils import BrowserUtils


class Contact_us_page(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.contact_us_button = (By.XPATH, "//a[text()=' Contact us']")
        self.get_in_touch = (By.XPATH, "//h2[contains(text(),'GET IN TOUCH')]")
        self.name = (By.XPATH, "//input[@data-qa = 'name']")
        self.email = (By.XPATH, "//input[@data-qa = 'email']")
        self.subject = (By.XPATH, "//input[@data-qa = 'subject']")
        self.message = (By.XPATH, "//textarea[@data-qa = 'message']")
        self.upload_button = (By.XPATH, "//input[@type='file']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
        self.success_message = (By.XPATH,"//div[@class='status alert alert-success']")
        self.home_button = (By.XPATH, "//a[text()=' Home']")


    def contact_us_page(self,file_path):
        #4. Click on 'Contact Us' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.contact_us_button))
        self.driver.find_element(*self.contact_us_button).click()

        #5. Verify 'GET IN TOUCH' is visible
        get_in_touch_text = self.driver.find_element(*self.get_in_touch).text
        assert get_in_touch_text == 'Get In Touch'

        #6. Enter name, email, subject and message
        self.driver.find_element(*self.name).send_keys('')
        self.driver.find_element(*self.email).send_keys('')
        self.driver.find_element(*self.subject).send_keys('')
        self.driver.find_element(*self.message).send_keys('')

        #7. Upload file
        self.driver.find_element(*self.upload_button).send_keys(file_path)

        #8. Click 'Submit' button
        self.driver.find_element(*self.submit_button).click()

        #9. Click OK button

        alert = self.driver.switch_to.alert
        wait.until(presence_of_element_located(alert))
        alert.accept()

        #10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        success_text = self.driver.find_element(*self.success_message).text
        assert 'Success' in success_text

        #11. Click 'Home' button and verify that landed to home page successfully
        self.driver.find_element(*self.home_button).click()








