import os
import time
import unittest
from selenium import webdriver

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_on_dashboard(self):
        user_login = LoginPage(self.driver)
        user_login.log_in('user10@getnada.com', 'Test-1234')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player()
        add_player = AddPlayer(self.driver)
        add_player.type_in_name("Lionel")
        add_player.type_in_surname("Messi")
        add_player.type_in_age("24/06/1987")
        add_player.type_in_main_position("forward")
        add_player.select_leg("right")
        add_player.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()