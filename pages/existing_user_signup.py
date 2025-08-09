from selenium.webdriver.common.by import By
from pages import signuploginpage
from pages.signuploginpage import load_json_data
import random
import logging


def get_random_user_to_signup():
    #Fetch random username and Email from json file 
    user_profile =  load_json_data()
    random_user = random.choice(user_profile)

    # random_user_name = random_user["Name"]
    # random_mail = random_user["Email"]

    return random_user

def verify_existing_user_signup_failed(browser_initialise):
    #Verify user signup for existing users failed
    failed_signup_msg = browser_initialise.find_element(By.XPATH, "//p[text()='Email Address already exist!']").text
    assert failed_signup_msg == "Email Address already exist!"
    logging.info("User is already exist, unable to signup...")




