import subprocess
import time
import pytest
from appium import webdriver
from utils.android_utils import android_get_desired_capabilities



@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)

# Замінив скоуп на function, при тестуванні логіну я думаю це опитмально
# Хотів би отримати фідбек на скільки це правильно або можливі варіанти вирішення проблемми
# Наприклад перевіряти авторизацію і виходити з аккаунта або при невдалій авторизації стирати поля
@pytest.fixture(scope='function')
def driver(run_appium_server):
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',android_get_desired_capabilities())
    yield driver
    driver.quit()
