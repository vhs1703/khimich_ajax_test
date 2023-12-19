import subprocess
import time
import pytest
from appium import webdriver
from utils.android_utils import android_get_desired_capabilities
from utils.logger_utils import get_logger


logger = get_logger()


@pytest.fixture(scope='session')
def run_appium_server():
    logger.info('Starting appium server')
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    logger.info('Appium server started')


