import json
from selenium.webdriver.common.by import By
import os
import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.user_data_generation import generate_complete_user_data
from selenium.webdriver.support import expected_conditions as EC


class SignupLoginPage:
    def __init__(self):
        self.signup_login_button = (By.CSS_SELECTOR, "a[href='/login']")
        self.new_user_signup_banner = (By.XPATH, "//h2[text()='New User Signup!']")
        self.input_name = (By.CSS_SELECTOR, "input[name='name']")
        self.email_addr = (By.CSS_SELECTOR,"input[type='email'][data-qa='signup-email'][name='email']")
        self.signup_button = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
        self.signup_form_banner = (By.XPATH, "//b[text()='Enter Account Information']")

        self.mr_radio_button = (By.CSS_SELECTOR, "input[id='id_gender1']")
        self.mrs_radio_button = (By.CSS_SELECTOR, "input[id='id_gender2']")
        self.password = (By.CSS_SELECTOR, "input[id='password']")
        self.day = (By.CSS_SELECTOR, "select[id='days']")
        self.month = (By.CSS_SELECTOR, "select[id='months']")
        self.year = (By.CSS_SELECTOR, "select[id='years']")
        self.firstname = (By.CSS_SELECTOR, "input[id='first_name']")
        self.lastname = (By.CSS_SELECTOR, "input[id='last_name']")
        self.company_name = (By.CSS_SELECTOR, "input[id='company']")
        self.addr_line1 = (By.CSS_SELECTOR, "input[id='address1']")
        self.addr_line2 = (By.CSS_SELECTOR, "input[id='address2']")
        self.country = (By.CSS_SELECTOR, "select[id='country']")
        self.state = (By.CSS_SELECTOR, "input[id='state']")
        self.city = (By.CSS_SELECTOR, "input[id='city']")
        self.zipcode = (By.CSS_SELECTOR, "input[id='zipcode']")
        self.mobile_number = (By.CSS_SELECTOR, "input[id='mobile_number']")
        self.create_account_button = (By.XPATH, "//button[@data-qa='create-account']")
        self.signup_success_banner = (By.XPATH, "//b[text()='Account Created!']")



    def click_signup_signin_button(self, browser_initialise): #Click signup/signin button in homepage
        browser_initialise.find_element(*self.signup_login_button).click()
        logging.info("Signup/Signin button clicked in home page")

    def signup_page(self, browser_initialise, user_data): #Fill first signup page
        assert browser_initialise.find_element(*self.new_user_signup_banner).text == "New User Signup!"
        browser_initialise.find_element(*self.input_name).send_keys(user_data["Name"])
        browser_initialise.find_element(*self.email_addr).send_keys(user_data["Email"])
        browser_initialise.find_element(*self.signup_button).click()
        #assert browser_initialise.find_element(*self.signup_form_banner).text == 'ENTER ACCOUNT INFORMATION'
        
    def verify_signup_form_visible(self, browser_initialise):
        wait = WebDriverWait(browser_initialise, 5)
        signip_form_msg = wait.until(EC.visibility_of_element_located(self.signup_form_banner))
        assert signip_form_msg.is_displayed
        logging.info("Signup form is visible, filling user details...")

    def fill_signup_form(self, browser_initialise, user_data):
        if user_data["Sex"] == "Male":
            browser_initialise.find_element(*self.mr_radio_button).click()
        else:
            browser_initialise.find_element(*self.mrs_radio_button).click()

        browser_initialise.find_element(*self.password).send_keys([user_data["Password"]])
        Select(browser_initialise.find_element(*self.day)).select_by_value(str(user_data["Day"]))
        Select(browser_initialise.find_element(*self.month)).select_by_value(str(user_data["Month"]))
        Select(browser_initialise.find_element(*self.year)).select_by_value(str(user_data["Year"]))
        browser_initialise.find_element(*self.firstname).send_keys(user_data["First Name"])
        browser_initialise.find_element(*self.lastname).send_keys(user_data["Last Name"])
        browser_initialise.find_element(*self.company_name).send_keys(user_data["Company"])
        browser_initialise.find_element(*self.addr_line1).send_keys(user_data["AddressLine1"])
        browser_initialise.find_element(*self.addr_line2).send_keys(user_data["AddressLine2"])
        Select(browser_initialise.find_element(*self.country)).select_by_value(user_data["Country"])
        browser_initialise.find_element(*self.state).send_keys(user_data["State"])
        browser_initialise.find_element(*self.city).send_keys(user_data["City"])
        browser_initialise.find_element(*self.zipcode).send_keys(user_data["Zipcode"])
        browser_initialise.find_element(*self.mobile_number).send_keys(user_data["Mobile Number"])
        browser_initialise.find_element(*self.create_account_button).click()

        wait = WebDriverWait(browser_initialise, 10)
        success_msg = wait.until(EC.visibility_of_element_located(self.signup_success_banner))
        assert success_msg.is_displayed()
        print("Account created successfully")


def load_json_data(json_file_path = "test_data/signup_form_data.json"):

    #json_file_path = "test_data/signup_form_data.json"

    #check whether json file present in given path
    if not os.path.exists(json_file_path):
        logging.info("json file is not present in the given path. Please check correct path")
        return []

    #open json file and load all user data and return
    with open(json_file_path, "r") as f:
        user_json_data = json.load(f)
        return user_json_data


