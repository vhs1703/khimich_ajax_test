from .page import Page
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.logger_utils import get_logger
from .login_page import LoginPage

logger = get_logger()




class MainPage(LoginPage):
    def __init__(self,driver : WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.logger = logger


    def open_sidebar(self):
        logger.info('Start oppening sidebar')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((MobileBy.ID,'com.ajaxsystems:id/menuDrawer'))
            )
        except:
            raise Exception('Sidebar button not found')
        sidebar_button=self.driver.find_element(by=MobileBy.ID,value='com.ajaxsystems:id/menuDrawer')
        sidebar_button.click()
        time.sleep(3)
        logger.info('Sidebar is opened')
        return True
    
    def is_sidebar_elements(self):
        return len(self.driver.find_elements(by=MobileBy.XPATH,value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/title"]'))
    
    def is_sidebar_button(self):
        return len(self.driver.find_element(by=MobileBy.ID,value='com.ajaxsystems:id/hubAdd').find_elements(by=MobileBy.XPATH,value='(//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"])'))
    
    def is_sidebar_button_clickable(self):
        sidebar_button = self.driver.find_element(by=MobileBy.ID,value='com.ajaxsystems:id/hubAdd').find_element(by=MobileBy.XPATH,value='(//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"])')
        return (sidebar_button.is_displayed(),sidebar_button.is_enabled())
    
    def is_sidebar_elements_clickable(self):
        sidebar_elements = self.driver.find_elements(by=MobileBy.XPATH,value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/title"]')
        return [(element.is_displayed(),element.is_enabled()) for element in sidebar_elements]
    
