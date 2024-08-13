import os
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

LINK = "https://capital.com/"
SHORT_LANGUAGES = ["ar", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh", "cn"]


LOGIN_BUTTON = By.ID, "wg_loginBtn"
EMAIL_FIELD = By.CSS_SELECTOR, "[name = 'email']"
PASSWORD_FIELD = By.CSS_SELECTOR, "[name = 'password']"
SUBMIT_LOGIN = By.CSS_SELECTOR, "form button.btn"
LOGO = By.CSS_SELECTOR, "logo.logo--capital"
COOKIE_REJECT_ALL = By.ID, "onetrust-reject-all-handler"
MY_ACCOUNT = By.ID, "wg_userarea"
TRADING_PLATFORM = By.CSS_SELECTOR, ".user-panel-content button.tradingPlatformBtn"


def do_login(driver):
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_FIELD).send_keys(os.getenv("EMAIL"))
    driver.find_element(*PASSWORD_FIELD).send_keys(os.getenv("PASSWORD"))
    driver.find_element(*SUBMIT_LOGIN).click()
    driver.find_element(*LOGO).click()


class TestMainPage():
    pass




