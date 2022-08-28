import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
# from pages.base_page import BasePage


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)

    # def test_log_in_to_the_system(self):
    #     user_login = LoginPage(self.driver)
    #     user_login.title_of_page()
    #     user_login.check_title_of_box()
    #     dashboard_page = Dashboard(self.driver)
    #     dashboard_page.title_of_page()
    #     base_page = BasePage(self.driver)
    #     base_page.assert_element_text()

    def test_log_in_to_the_site(self):
        self.user_login.title_of_page()
        self.user_login.check_title_of_box()
        self.user_login.log_in('user10@getnada.com', 'Test-1234')
        self.dashboard_page.title_of_page()
        time.sleep(4)

    def test_invalid_password_to_log_in(self):
        self.user_login.log_in('user10@getnada.com', 'Test-1111')
        self.user_login.invalid_password_check_message()
        time.sleep(2)
        self.user_login.title_of_page()
        time.sleep(4)

    def test_empty_login(self):
        self.user_login.log_in('', '1234')
        self.user_login.empty_login_check_message()
        self.user_login.title_of_page()
        time.sleep(4)

    def check_sign_in_button_text(self):
        self.user_login.title_of_page()
        self.user_login.assert_sign_in_text()
        self.user_login.title_of_page()
        time.sleep(4)

    def select_language(self, language):
        self.user_login.click_on_language_listbox()
        if language == "Polski":
            self.user_login.click_on_the_element(self.user_login.dropdown_polski_xpath)
        else:
            self.user_login.click_on_the_element(self.user_login.dropdown_english_xpath)
        time.sleep(4)

    def test_log_out(self):
        self.user_login.log_in('user10@getnada.com', 'Test-1234')
        self.dashboard_page.wait_for_sign_out_is_visible()
        time.sleep(2)
        self.dashboard_page.click_on_sign_out_button()
        self.user_login.title_of_page()
        time.sleep(4)

    # def assert_sign_in_text(self):
    #     self.assert_element_text(self.driver, self.user_login.sign_in_button_xpath, self.user_login.sign_in_button_text)
    #
    @classmethod
    def tearDown(cls):
        cls.driver.quit()