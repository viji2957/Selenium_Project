import logging
from pages.delete_user_account import delete_user, remove_user_from_json

def test_delete_user_account(browser_initialise):

    #delete user from website and store return email in variable
    login_mail = delete_user(browser_initialise)
    
    #remove user details from json file
    remove_user_from_json(login_mail)