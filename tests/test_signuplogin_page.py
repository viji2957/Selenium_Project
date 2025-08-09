import pytest
from pages.signuploginpage import SignupLoginPage, load_json_data
from utils.user_data_generation import FakeUserData, generate_complete_user_data, append_user_data_to_json

def test_user_signup(browser_initialise, generate_complete_user_data):
    signup_login = SignupLoginPage() #class object variable
    signup_login.click_signup_signin_button(browser_initialise) #homepage to signup/login page
    append_user_data_to_json(generate_complete_user_data)
    signup_login.signup_page(browser_initialise, generate_complete_user_data) #signup page to signup form fill page
    signup_login.verify_signup_form_visible(browser_initialise)
    signup_login.fill_signup_form(browser_initialise, generate_complete_user_data)


