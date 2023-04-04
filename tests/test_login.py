import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("start_appium_server")
class TestAndroidDeviceLocal:
    def test_click_first(self):
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()

    def test_enter_value(self):
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1").send_keys("Hello World")

    def test_submit(self):
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1").click()

    def test_back(self):
        self.driver.back()

    def test_scroll_tab(self):
        self.driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView").click()

    def test_swipe(self):
        self.driver.swipe(540, 1740, 540, 540)