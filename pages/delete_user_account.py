import logging
from selenium.webdriver.common.by import By
from pages.login_page import get_random_user_credential, login_with_user_credential, logout_account, gen_wrong_username_credential, gen_wrong_password_credential
from pages.signuploginpage import load_json_data
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def delete_user(browser_initialise):

    #get credentials and log-in into account
    login_email, login_password = get_random_user_credential()
    login_with_user_credential(browser_initialise, login_email, login_password)
    logging.info("User is successfully logged-in")
    assert "Logged in as" in browser_initialise.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text

    #delete user account
    delete_button = browser_initialise.find_element(By.XPATH, "//a[@href='/delete_account']")
    delete_button.click()
    delete_banner = (By.XPATH, "//h2//b[text()='Account Deleted!']")
    wait = WebDriverWait(browser_initialise, 5)
    delete_msg = wait.until(EC.visibility_of_element_located(delete_banner))
    assert delete_msg.is_displayed()
    logging.info(f"Account deleted successfuly for login ID {login_email}")
    return login_email


def remove_user_from_json(login_email, json_file_path = "test_data/signup_form_data.json"):
    
    #collect all users details from json to variable
    all_users = load_json_data()

    #delete user profile details from DB
    #updated_users = [user for user in all_users if user["Email"] != login_email]
    for user in all_users:
        if user.get("Email") == login_email:
            all_users.remove(user)
            logging.info(f"user profile is removed for user email: {login_email}")
            break
        else:
            logging.info(f"No user found with email: {login_email}")

    with open(json_file_path, 'w') as f:
        json.dump(all_users, f, indent=4)




