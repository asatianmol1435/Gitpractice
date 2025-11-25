import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserUtils import BrowserUtils


class SignUp(BrowserUtils):

    def __init__(self,driver):
        self.driver = driver
        self.new_user_signup_button = (By.XPATH, "//a[text()=' Signup / Login']")
        self.signup_title = (By.XPATH, "//h2[text()='New User Signup!']")
        self.name = (By.XPATH, "//input[@name = 'name']")
        self.email = (By.XPATH, "//input[@data-qa = 'signup-email']")
        self.signup_button = (By.XPATH, "//button[@data-qa = 'signup-button']")
        self.title_radio_button = (By.XPATH, "//input[@value = 'Mr']")
        self.password = (By.XPATH, "//input[@id = 'password']")
        self.days = (By.XPATH, "//select[@id = 'days']")
        self.months = (By.XPATH, "//select[@id = 'months']")
        self.year = (By.XPATH, "//select[@id = 'years']")
        self.newsletter_checkbox = (By.XPATH, "//input[@name = 'newsletter']")
        self.offers_checkbox = (By.XPATH, "//input[@name = 'optin']")
        self.first_name = (By.XPATH, "//input[@id = 'first_name']")
        self.last_name = (By.XPATH, "//input[@id = 'last_name']")
        self.company = (By.XPATH, "//input[@id = 'company']")
        self.address1 = (By.XPATH, "//input[@id = 'address1']")
        self.address2 = (By.XPATH, "//input[@id = 'address2']")
        self.state = (By.XPATH, "//input[@id = 'state']")
        self.city = (By.XPATH, "//input[@id = 'city']")
        self.zipcode = (By.XPATH, "//input[@id = 'zipcode']")
        self.mobile_num = (By.XPATH, "//input[@id = 'mobile_number']")
        self.create_button = (By.XPATH, "//button[@data-qa = 'create-account']")
        self.continue_button = (By.XPATH, "//a[@data-qa = 'continue-button']")
        self.logged_user_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")
        self.delete_button = (By.XPATH, "//a[text() = ' Delete Account']")
        self.delete_confirmation_text = (By.XPATH, "//a[text() = 'Account Deleted!']")
        self.delete_continue_button = (By.XPATH, "//a[@data-qa = 'continue-button']")
        self.user_exists = (By.XPATH, "//p[text()='Email Address already exist!']")


    def signup_page(self, name, email):
        # 4. Click on 'Signup / Login' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.new_user_signup_button))
        self.driver.find_element(*self.new_user_signup_button).click()

        self.driver.find_element(*self.signup_button).click()

        # 5. Verify 'New User Signup!' is visible
        signup_title = self.driver.find_element(*self.signup_title)
        assert signup_title.is_displayed()

        # 6. Enter name and email address
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)

        # 7. Click 'Signup' button
        self.driver.find_element(*self.signup_button).click()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        # user_details_title = driver.find_element(By.XPATH, "//b[text()='Enter Account Information']").text
        # time.sleep(4)
        # assert user_details_title == "Enter Account Information"

    def signup_information_page(self,password,first_name,last_name,company,address1,address2,state,city,zipcode,mobile_num):
        # 9. Fill details: Title, Name, Email, Password, Date of birth
        self.driver.find_element(*self.title_radio_button).click()
        # driver.find_element(By.XPATH, "//input[@id = 'name']").clear
        # driver.find_element(By.XPATH, "//input[@id = 'name']").send_keys("Anmol Asati")
        # driver.find_element(By.XPATH, "//input[@id = 'email']").send_keys("anmolasati@gmail.com")
        self.driver.find_element(*self.password).send_keys(password)
        days_dropdown = Select(self.driver.find_element(*self.days))
        days_dropdown.select_by_value("20")
        months_dropdown = Select(self.driver.find_element(*self.months))
        months_dropdown.select_by_visible_text("June")
        years_dropdown = Select(self.driver.find_element(*self.year))
        years_dropdown.select_by_value("1999")

        # 10. Select checkbox 'Sign up for our newsletter!'
        self.driver.find_element(*self.newsletter_checkbox).click()

        # 11. Select checkbox 'Receive special offers from our partners!'
        self.driver.find_element(*self.offers_checkbox).click()

        # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.company).send_keys(company)
        self.driver.find_element(*self.address1).send_keys(address1)
        self.driver.find_element(*self.address2).send_keys(address2)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.mobile_num).send_keys(mobile_num)

        # 13. Click 'Create Account button'
        self.driver.find_element(*self.create_button).click()


    def signup_confirmation_page(self):

        # 14. Verify that 'ACCOUNT CREATED!' is visible
        # account_created_text = driver.find_element(By.XPATH, "//b[text() = 'Account Created!']").text
        # assert account_created_text == "Account Created!"

        # 15. Click 'Continue' button
        self.driver.find_element(*self.continue_button).click()


    def verify_logged_in_page(self):


        # 16. Verify that 'Logged in as username' is visible
        logged_user = self.driver.find_element(*self.logged_user_text).text
        assert "Anmol Asati" in logged_user


    def already_registered_user(self,name,email):
        # 4. Click on 'Signup / Login' button
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located(self.new_user_signup_button))
        self.driver.find_element(*self.new_user_signup_button).click()

        self.driver.find_element(*self.signup_button).click()

        # 5. Verify 'New User Signup!' is visible
        signup_title = self.driver.find_element(*self.signup_title)
        assert signup_title.is_displayed()

        # 6. Enter name and email address
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)

        # 7. Click 'Signup' button
        self.driver.find_element(*self.signup_button).click()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        # user_details_title = driver.find_element(By.XPATH, "//b[text()='Enter Account Information']").text
        # time.sleep(4)
        # assert user_details_title == "Enter Account Information"

        #8. Verify error 'Email Address already exist!' is visible
        already_user_exists = self.driver.find_element(*self.user_exists).text
        assert already_user_exists == "Email Address already exist!"






