from .page import Page
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.logger_utils import get_logger




class LoginPage(Page):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = get_logger()

        self.logger.info('Waiting untill app loads')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"]'))
            )
        except:
            raise Exception('App was not loaded')
        self.logger.info('App loads')
        #Чому вирішив використати саме find_elements, в XPATH можна було б додати and @text='Вхід',але я врахував те
        #Що може тестуватись іншомовна версія додатку,тобто текст буде на іншій мові

        login_button = self.driver.find_elements(by=MobileBy.XPATH,value='//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"]')[0]
        login_button.click()
        self.logger.info('Login button clicked')
        return
    

    def auth(self,login:str,password:str):
        if not isinstance(login,(str)) or not isinstance(password,(str)):
            raise TypeError('Both arguments must be str')
        
        if len(password) <10:
            raise ValueError('Password len must be more than 10 symbols')

        if any(char.isalpha() for char in password) == False:
            raise ValueError('Password must contains letters')
        

        login_input = self.driver.find_element(by=MobileBy.ID,value='com.ajaxsystems:id/authLoginEmail').find_element(by=MobileBy.CLASS_NAME,value='android.widget.EditText')
        login_input.send_keys(login)
        self.logger.info('Login sended to input')

        # Незнаю на скільки доречно використовувати time.sleep в тестуванні,хотів би отримати фідбек
        time.sleep(1)

        password_input = self.driver.find_element(by=MobileBy.ID,value='com.ajaxsystems:id/authLoginPassword').find_element(by=MobileBy.CLASS_NAME,value='android.widget.EditText')
        password_input.send_keys(password)
        self.logger.info('Password sended to input')

        time.sleep(1)

        submit_button = self.driver.find_element(by=MobileBy.XPATH,value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ajaxsystems:id/bottomContent"]').find_element(by=MobileBy.CLASS_NAME,value='android.widget.Button')
        submit_button.click()
        self.logger.info('Form submited, start waiting for login result')
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH,'//android.view.ViewGroup[@resource-id="com.ajaxsystems:id/hubAdd"]')))
        except:
            self.logger.debug('Login error')
            # Тобто не авторизовались, неправильний пароль або логін
            return False
        # При успішній авторизації ми побачимо наступну сторінку де буде певна кнопка або елемент
        # Якщо за умовних 20 секунд знайшли цей елемент - авторизація успішна
        self.logger.info('Login sucsess')
        return True

