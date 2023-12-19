import subprocess
import re

# Функція написана тільки для одного телефону, немає змоги підключити більше
# Через те що використовую re, можна розширити, в matches буде знаходитись список із всіх uid підключених


def get_udid():
    result = subprocess.run('adb devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout
    pattern = re.compile(r'\b(\w+)\s+device\b')
    matches = pattern.findall(output)
    udid = matches[0] if matches else None
    return udid

def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
