import logging
from selenium.webdriver.common.by import By
from pages.login_page import get_random_user_credential, login_with_user_credential, logout_account, gen_wrong_username_credential, gen_wrong_password_credential


def test_login_with_credential(browser_initialise):
    login_email, login_password = get_random_user_credential()
    login_with_user_credential(browser_initialise, login_email, login_password)
    logging.info("User is successfully logged-in")
    assert "Logged in as" in browser_initialise.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
    logout_account(browser_initialise)








