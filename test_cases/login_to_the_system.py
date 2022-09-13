import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
def cookieClicker():
    s = Service("C:/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

from selenium.webdriver.chrome.service import Service

class TestLoginPage(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service("C:/chromedriver/chromedriver.exe"))
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)
        self.base_page = BasePage(self.driver)

    def test_log_in_to_the_site(self):
        self.user_login.title_of_page()
        self.user_login.check_title_of_box()
        self.user_login.log_in('user10@getnada.com', 'Test-1234')
        self.dashboard_page.title_of_page()
        time.sleep(4)

    def test_invalid_password_to_log_in(self):
        self.user_login.log_in('user10@getnada.com', 'Test-1111')
        if self.user_login.invalid_password_check_message():
            print("Invalid password to log in")
        else:
            print("Try again")
        time.sleep(2)
        self.user_login.title_of_page()
        time.sleep(2)

    def test_text(self):
        self.base_page.get_element_text(self.driver, "//*[@id='__next']/form/div/div[1]/h5")

    def test_empty_login(self):
        self.user_login.log_in('', '1234')
        if self.user_login.empty_login_check_message():
            print("User didn't type in login")
        else:
            print("Try again")
        time.sleep(2)
        self.user_login.title_of_page()
        time.sleep(2)

    def test_text_box_title(self):
        self.user_login.title_of_page()
        if self.user_login.check_title_of_box():
            print("Well done")
        else:
            print("Try again")
        time.sleep(2)

    def test_select_polish_language(self):
        self.user_login.title_of_page()
        self.user_login.select_language("Polski")
        time.sleep(4)

    def test_log_out(self):
        self.user_login.log_in('user10@getnada.com', 'Test-1234')
        self.dashboard_page.wait_for_sign_out_is_visible()
        self.dashboard_page.title_of_page()
        self.dashboard_page.click_on_sign_out_button()
        self.user_login.title_of_page()
        time.sleep(4)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()