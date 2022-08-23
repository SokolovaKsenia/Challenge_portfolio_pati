from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        # self.driver.get("https://scouts-test.futbolkolektyw.pl")
        expected_text = "Scouts Panel"
        element_xpath = "//*[text()= 'Scouts Panel']"
        element = driver.find_element(by=By.XPATH, value=element_xpath)
        element_text = element.text
        assert expected_text == element_text
