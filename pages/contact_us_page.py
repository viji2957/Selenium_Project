from selenium.webdriver.common.by import By
import logging
from pages.existing_user_signup import get_random_user_to_signup
from utils.contact_us_data_generation import contact_us_message, contact_us_subject
import os
from selenium.common.exceptions import NoAlertPresentException

class ContactUs:
    def __init__(self):
        #all required locators from contact us
        self.contactus_button = (By.LINK_TEXT, "Contact us")

        self.contact_us_title = (By.XPATH, "//h2[@class='title text-center'][contains(., 'Contact')]")
        self.name_locator = (By.CSS_SELECTOR, "input[name='name']")
        self.email_locator = (By.CSS_SELECTOR, "input[name='email']")
        self.subject_locator = (By.CSS_SELECTOR, "input[name='subject']")
        self.message_locator = (By.CSS_SELECTOR, "textarea[name='message']")
        self.file_locator = (By.CSS_SELECTOR, "input[name='upload_file']")
        self.submit_button_locator = (By.CSS_SELECTOR, "input[name='submit']")
        self.contact_us_success_locator = (By.XPATH, "//div[@class='status alert alert-success']")
    
    def click_contactus(self, browser_initialise):
        #Click contact us button from home page
        browser_initialise.find_element(*self.contactus_button).click()
        logging.info("Clicking Contact Us button from Homepage")

    def check_in_contact_us_page(self, browser_initialise):
        #check entered in contact us page
        title = browser_initialise.find_element(*self.contact_us_title).text
        assert "CONTACT" in title
        logging.info("Entered into Contact Us page, please fill contact us form...")

    def fill_contact_us_form(self, browser_initialise):
        #Absolute file path
        file_path = "C:\\Users\\vijbs\\Documents\\hosts.txt"

        #get required data to fill contact us form
        user_data = get_random_user_to_signup()
        subject = contact_us_subject()
        message = contact_us_message()

        #fill out contact us form fields
        browser_initialise.find_element(*self.name_locator).send_keys(user_data["Name"])
        browser_initialise.find_element(*self.email_locator).send_keys(user_data["Email"])
        browser_initialise.find_element(*self.subject_locator).send_keys(subject)
        browser_initialise.find_element(*self.message_locator).send_keys(message)

        #Checking file existions in absolute path
        if not os.path.exists(file_path):
            logging.info("File does not exist to attach in Contact Us attachment, please check...")
            raise FileNotFoundError(f"Attachment not found in given path: {file_path}")
        
        #attach/upload file
        browser_initialise.find_element(*self.file_locator).send_keys(file_path)
        logging.info("Contact us file attached successfully...")

    def click_submit_button(self, browser_initialise):
        #Click submit button on contact us page
        browser_initialise.find_element(*self.submit_button_locator).click()
        logging.info("Clicking on Contact Us submit button")

        #Accept java alert after submit button
        try:
            alert = browser_initialise.switch_to.alert
            alert_text = alert.text
            assert "proceed" in alert_text, f"alert appeared with text: {alert_text}"
            logging.info(f"Java pop-up for proceeding information appeared with text: {alert_text}")
            alert.accept()
            logging.info("Java pop-up message accepted...")

        except NoAlertPresentException:
            logging.error("Expected JavaScript alert did not appear after submitting the form.")
            assert False, "No alert present after form submission"

    def verify_contact_us_success(self, browser_initialise):
        #Verify contact is form submitted successfully
        contact_us_success = browser_initialise.find_element(*self.contact_us_success_locator).text
        assert "Success" in contact_us_subject
        logging.info("Success! Your details have been submitted successfully...")




