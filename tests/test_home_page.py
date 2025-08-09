from selenium.webdriver.common.by import By


def test_home_signup_login(browser_initialise):
    title_verify = browser_initialise.title
    assert title_verify == "Automation Exercise"

