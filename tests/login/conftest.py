import pytest

from framework.login_page import LoginPage

from appium import webdriver
from utils.android_utils import android_get_desired_capabilities
from utils.logger_utils import get_logger


logger = get_logger()





# Замінив скоуп на function, при тестуванні логіну я думаю це опитмально
# Хотів би отримати фідбек на скільки це правильно або можливі варіанти вирішення проблемми
# Наприклад перевіряти авторизацію і виходити з аккаунта або при невдалій авторизації стирати поля
@pytest.fixture(scope='function')
def login_driver(run_appium_server):
    caps = android_get_desired_capabilities()
    logger.info(f'Starting appium driver with udid {caps.get("udid")}')
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
    logger.info('Appium driver started')
    yield driver
    driver.quit()
    logger.info('Appium driver closed')



@pytest.fixture(scope='function')
def user_login_fixture(login_driver):
    yield LoginPage(login_driver)
    
