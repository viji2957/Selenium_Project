import time
from selenium import webdriver
import pytest
import os
import datetime
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser_initialise(request):
    headless = request.config.getoption("--headless")
    driver_control = initialize_chrome(headless)
    driver_control.implicitly_wait(5)
    driver_control.get("https://www.automationexercise.com/")
    logging.info("Home page loaded successfully...")
    yield driver_control

    time.sleep(2)
    driver_control.quit()

def initialize_chrome(headless = False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver_control = webdriver.Chrome(options=options)
    return driver_control

def pytest_addoption(parser):
    parser.addoption("--loglevel", action = "store", default = "INFO", help = "Set the logging level")
    parser.addoption("--headless", action = "store_true", default = False, help = "Run test in healdess")


def pytest_configure(config):
    #report_dir = "reports"
    #root_dir = os.path.dirname(os.path.abspath(__file__))
    #reports_dir = os.path.join(root_dir, "reports")
    log_level = config.getoption("loglevel").upper()
    
    if not os.path.exists("reports"):
        os.makedirs("reports")

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    default_report_path = f"reports/log_{now}.html"
    config.option.htmlpath = default_report_path
    config.option.self_contained_html = True

    # Configure Python logging
    logging.basicConfig(
        filename=default_report_path,
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

