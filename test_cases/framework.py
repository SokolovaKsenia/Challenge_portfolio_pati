import os
import unittest

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.get("https://scouts-test.futbolkolektyw.pl/en")
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")


class TestMediumPage(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.get("https://medium.com/")
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title("https://medium.com/")
        expected_title = "Medium – Where good ideas find you."
        assert actual_title == expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
