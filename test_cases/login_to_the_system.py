import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
# from pages.base_page import BasePage


class TestLoginPage(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_box()
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        # base_page = BasePage(self.driver)
        # base_page.assert_element_text()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
