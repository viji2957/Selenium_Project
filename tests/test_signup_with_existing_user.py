from pages.signuploginpage import SignupLoginPage
from pages.existing_user_signup import get_random_user_to_signup, verify_existing_user_signup_failed


def test_signup_with_existing_user(browser_initialise):

    signup_login_page = SignupLoginPage()
    signup_login_page.click_signup_signin_button(browser_initialise)
    userdata = get_random_user_to_signup()
    signup_login_page.signup_page(browser_initialise, userdata)
    verify_existing_user_signup_failed(browser_initialise)



