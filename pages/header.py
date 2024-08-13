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


class MainPageLocators:
    LOGIN_BUTTON = By.ID, "wg_loginBtn"
    EMAIL_FIELD = By.CSS_SELECTOR, "[name = 'email']"
    PASSWORD_FIELD = By.CSS_SELECTOR, "[name = 'password']"
    SUBMIT_LOGIN = By.CSS_SELECTOR, "form button.btn"
    LOGO = By.CSS_SELECTOR, "logo.logo--capital"
    COOKIE_REJECT_ALL = By.ID, "onetrust-reject-all-handler"
    MY_ACCOUNT = By.ID, "wg_userarea"
    TRADING_PLATFORM = By.CSS_SELECTOR, ".user-panel-content button.tradingPlatformBtn"


# class Menu:
#     PRODUCTS_AND_SERVICES =
#     # DEMO_ACCOUNT =

def do_login(driver):
    # ЭТО НАДО ПЕРЕПИСАТЬ ЧЕРЕЗ КУКИ

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_FIELD).send_keys(os.getenv("EMAIL"))
    driver.find_element(*PASSWORD_FIELD).send_keys(os.getenv("PASSWORD"))
    driver.find_element(*SUBMIT_LOGIN).click()
    driver.find_element(*LOGO).click()


class TestMenu():
    # test Header Menu

    def test_pages_in_products_and_services(self, driver):
        """doc string."""
        driver.get(LINK)
        actions = ActionChains(driver)
        # desired_elem = "sda"
        # actions.move_to_element(desired_elem).perform()

        # Product and services
        PRODUCT_AND_SERVICES = (By.CSS_SELECTOR, '[data-type="nav_id2"]')
        # driver.find_element(*PRODUCT_AND_SERVICES).click()
        # assert "trading-products" in driver.current_url
        # time.sleep(5)

        pr_button = driver.find_element(*PRODUCT_AND_SERVICES)
        actions.move_to_element(pr_button).perform()
        # actions.move_to_element(By.CSS_SELECTOR, '[data-type="nav_id2"]')
        DEMO_ACCOUNT = By.CSS_SELECTOR, '[data-type="nav_id578"]'
        driver.find_element(*DEMO_ACCOUNT).click()
        time.sleep(99)
        # 'data-type="nav_id578"'
        # # Markets
        # 'data-type="nav_id3"'

    pass


class TestLanguagesAndCountries():
    # test Dropdown [Languages & Countries]

    # СДЕЛАТЬ ЧТОБЫ 1 РАЗ БРАУЗЕР ОТКРЫВАЛСЯ
    @pytest.mark.skip
    @pytest.mark.parametrize("lg", SHORT_LANGUAGES)
    def test_switch_language(self, driver, lg):
        driver.get(LINK)
        # actions = ActionChains(driver)
        # desired_elem = "sda"
        # actions.move_to_element(desired_elem).perform()

        driver.find_element(By.CSS_SELECTOR, "div.licLangSw__btn").click()
        driver.find_element(By.CSS_SELECTOR, f"a[data-type='nav_lang_{lg}']").click()
        assert f"capital.com/{lg}" in driver.current_url


class TestAccount():
    # test "Log in", "Sign up" and "My account" menu

    @pytest.mark.skip
    def test_go_to_traiding_trought_my_account(self, driver):
        driver.get(LINK)
        wait = WebDriverWait(driver, 10)

        do_login(driver)
        assert "capital.com/trading/platform" in driver.current_url

        driver.switch_to.window(driver.window_handles[1])
        # time.sleep(999)

        try:
            wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()
        except:
            pass

        driver.find_element(*MY_ACCOUNT).click()
        driver.find_element(*TRADING_PLATFORM).click()
        assert "capital.com/trading/platform" in driver.current_url


class TestLogoAndMessage():
    # test Logo and Message above menu
    pass
