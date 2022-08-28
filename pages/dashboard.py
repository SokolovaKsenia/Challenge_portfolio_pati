import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    dev_team_contact_hyperlink_xpath = "// a[contains(@ href, '://')]"
    logo_scouts_panel_xpath = "//*[contains(@class, 'MuiCardMedia')]"
    add_player_hyperlink_xpath = "//*[2][name()='a']"
    super_man_hyperlink_xpath = "//h6//following-sibling::a[1]"
    scouts_panel_xpath = "//*[text()='Scouts Panel']"
    scouts_panel_header_xpath = "//div[1]/header/div/h6"
    main_page_icon_xpath = "//*[@class='MuiSvgIcon-root jss29 jss30']"
    main_page_button_xpath = "//ul[1]/div[1]"
    main_page_xpath = "//*[text()='Main page']"
    polski_button_xpath = "//*[text()='Polski']"
    matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    left_sidebar_xpath = "//*[contains(@class, 'MuiPaper-elevation0')]"
    header_xpath = "//div[1]/header/div"
    sign_out_button_xpath = "//*[contains(@class, 'MuiListItem-button')]"
    players_count_field_xpath = "//*[contains(@class, 'MuiGrid-grid-md')]"
    shortcuts_block_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div"
    reports_count_field_xpath = "//main/div[2]/div[3]/div"
    scouts_panel_description_xpath = "//*[contains(@class, 'TextSecondary')]"
    sign_out_menu_xpath = "(//ul[contains(@class, 'MuiList-root')])[2]/div[2]/div/span"
    add_player_button_xpath = "//*[text()='Add player']"
    # element_text = 'Scouts Panel'
    # element_text_xpath = "//*[@id='__next']/div[1]/header/div/h6"

    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
    element_text = 'Scouts Panel'
    element_text_xpath = '//*[@id="__next"]/form/div/div[1]/h5'
    wait = WebDriverWait(driver, 7)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.logo_scouts_panel_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_on_add_player(self):
        self.click_on_the_element(self.add_player_button_xpath)
    def click_on_the_main_page_icon_xpath(self):
        self.click_on_the_element(self.main_page_icon_xpath)
    def visibility_of_element_located(self):
        self.click_on_the_element(self.players_count_field_xpath)

    def wait_for_sign_out_is_visible(self):
        self.wait_for_element_to_be_visible(self.sign_out_menu_xpath)

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_menu_xpath)

