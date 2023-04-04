import pytest
from utilities import read_utils
from appium import webdriver


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        dic = read_utils.get_value_from_json()
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic)
        driver.implicitly_wait(10)
