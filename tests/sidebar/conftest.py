import pytest
from appium import webdriver
from utils.android_utils import android_get_desired_capabilities
from utils.logger_utils import get_logger
from framework.main_page import MainPage

logger = get_logger()


@pytest.fixture(scope='session')
def driver(run_appium_server):
    caps = android_get_desired_capabilities()
    logger.info(f'Starting appium driver with udid {caps.get("udid")}')
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
    logger.info('Appium driver started')
    yield driver
    driver.quit()
    logger.info('Appium driver closed')



@pytest.fixture(scope='session')
def main_page_fixture(driver):
    mainpage = MainPage(driver)
    mainpage.auth(login='qa.ajax.app.automation@gmail.com',password='qa_automation_password')
    mainpage.open_sidebar()
    yield mainpage