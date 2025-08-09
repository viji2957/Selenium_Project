import logging
from selenium.webdriver.common.by import By
from pages.login_page import get_random_user_credential, login_with_user_credential, logout_account, gen_wrong_username_credential, gen_wrong_password_credential

def test_login_with_wrong_password(browser_initialise):

    correct_username, wrong_password = gen_wrong_password_credential()
    login_with_user_credential(browser_initialise, correct_username, wrong_password)

    text = browser_initialise.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']").text
    assert "Your email or password is incorrect" in text
    logging.info("Given username is wrong, please check...")
