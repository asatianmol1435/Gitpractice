import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserUtils import BrowserUtils


class Login_page(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.new_user_signup_button = (By.XPATH, "//a[text()=' Signup / Login']")
        self.signup_title = (By.XPATH, "//h2[text()='New User Signup!']")
        self.signup_button = (By.XPATH, "//button[@data-qa = 'signup-button']")
        self.login_title = (By.XPATH, "//h2[text()='Login to your account']")
        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")
        self.wrong_id_error = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
        self.logout_button = (By.XPATH, "//a[text()=' Logout']")



    def login(self,login_email,login_password):
        # 4. Click on 'Signup / Login' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.new_user_signup_button))
        self.driver.find_element(*self.new_user_signup_button).click()

        self.driver.find_element(*self.signup_button).click()

        #5. Verify 'Login to your account' is visible
        login_title = self.driver.find_element(*self.login_title)
        assert login_title.is_displayed()

        #6. Enter correct email address and password
        self.driver.find_element(*self.login_email).clear()
        self.driver.find_element(*self.login_email).send_keys(login_email)
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(login_password)

        #7. Click 'login' button
        self.driver.find_element(*self.login_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
        expected_url = "https://automationexercise.com/login"
        assert self.driver.current_url == expected_url

    def wrong_login(self,wrong_login_email,wrong_login_password):
        # 4. Click on 'Signup / Login' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.new_user_signup_button))
        self.driver.find_element(*self.new_user_signup_button).click()

        self.driver.find_element(*self.signup_button).click()

        # 5. Verify 'Login to your account' is visible
        login_title = self.driver.find_element(*self.login_title)
        assert login_title.is_displayed()

        #6. Enter incorrect email address and password
        self.driver.find_element(*self.login_email).clear()
        self.driver.find_element(*self.login_email).send_keys(wrong_login_email)
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(wrong_login_password)

        #7. Click 'login' button
        self.driver.find_element(*self.login_button).click()

        #8. Verify error 'Your email or password is incorrect!' is visible
        invalid_login_text = self.driver.find_element(*self.wrong_id_error).text
        assert invalid_login_text == 'Your email or password is incorrect!'



