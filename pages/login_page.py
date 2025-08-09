from selenium.webdriver.common.by import By
from pages import signuploginpage
from pages.signuploginpage import load_json_data
import random


def get_random_user_credential():
    user_profile =  load_json_data()
    random_user = random.choice(user_profile)

    random_user_name = random_user["Email"]
    random_password = random_user["Password"]

    return random_user_name, random_password

def gen_wrong_username_credential():
    user_profile =  load_json_data()
    random_user = random.choice(user_profile)

    random_user_name = random_user["Email"]
    wrong_user_name = "invalid" + random_user_name
    random_password = random_user["Password"]
    return wrong_user_name, random_password

def gen_wrong_password_credential():
    user_profile =  load_json_data()
    random_user = random.choice(user_profile)

    random_user_name = random_user["Email"]
    random_password = random_user["Password"]
    wrong_password = "wrong" + random_password
    return random_user_name, wrong_password

def login_with_user_credential(browser_initialise, login_email, login_password):
    signup_login = signuploginpage.SignupLoginPage()
    signup_login.click_signup_signin_button(browser_initialise)

    login_banner = browser_initialise.find_element(By.XPATH, "//h2[text()='Login to your account']").text
    assert login_banner == "Login to your account"

    browser_initialise.find_element(By.XPATH, "//form[@action='/login']//input[@name='email']").send_keys(login_email)
    browser_initialise.find_element(By.XPATH, "//form[@action='/login']//input[@name='password']").send_keys(login_password)
    browser_initialise.find_element(By.XPATH, "//form[@action='/login']//button[@data-qa='login-button']").click()

def logout_account(browser_initialise):
    browser_initialise.find_element(By.XPATH, "//a[@href='/logout']").click()
    print("User is successfully logged out")





