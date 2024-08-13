import pytest
from selenium import webdriver
from selenium.common import TimeoutException


# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# should be as a decorator
# def try_TimeoutException():
#     try:
#         yield
#     except TimeoutException:
#         pass sdfsdfs
