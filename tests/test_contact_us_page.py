from pages.contact_us_page import ContactUs
import logging

def test_contact_us(browser_initialise):
    #Verify landed into home_page
    title_verify = browser_initialise.title
    assert title_verify == "Automation Exercise"

    contact_us = ContactUs()
    contact_us.click_contactus(browser_initialise)
    logging.info("Contact Us link button clicked in homepage...")

    contact_us.check_in_contact_us_page(browser_initialise)
    logging.info("Please fill required details...")

    contact_us.fill_contact_us_form(browser_initialise)
    logging.info("Required details are filled in Contact Us form...")

    contact_us.click_submit_button(browser_initialise)
    logging.info("Contact us form details are submitted...")
