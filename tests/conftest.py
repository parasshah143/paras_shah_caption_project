from appium import webdriver
import pytest
from utilities import read_utils


@pytest.fixture(scope="class", autouse=True)
def start_appium_server(request):
    dic = read_utils.get_value_from_json()
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()
