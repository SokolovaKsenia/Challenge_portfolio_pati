import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
    element_text = 'Scouts Panel'
    element_text_xpath = "//*[@id='__next']/div[1]/header/div/h6"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    # dev_team_contact_hyperlink_xpath = "// a[contains(@ href, '://')]"
    # logo_scouts_panel_xpath = "//*[contains(@class, 'MuiCardMedia')]"
    # add_player_hyperlink_xpath = "//*[2][name()='a']"
    # super_man_hyperlink_xpath = "//h6//following-sibling::a[1]"
    # scouts_panel_xpath = "//*[text()='Scouts Panel']"
    # scouts_panel_header_xpath = "//div[1]/header/div/h6"
    # main_page_icon_xpath = "//*[@class='MuiSvgIcon-root jss29 jss30']"
    # main_page_button_xpath = "//ul[1]/div[1]"
    # main_page_xpath = "//*[text()='Main page']"
    # polski_button_xpath = "//*[text()='Polski']"
    # matches_count_xpath = "//div[2]/div[2]/div/div[1]"
    # left_sidebar_xpath = "//*[contains(@class, 'MuiPaper-elevation0')]"
    # header_xpath = "//div[1]/header/div"
    # sign_out_button_xpath = "//*[contains(@class, 'MuiListItem-button')]"
    # players_count_field_xpath = "//*[contains(@class, 'MuiGrid-grid-md')]"
    # last_created_player_xpath = "//h6"
    # shortcuts_block_xpath = "//*[@class='MuiCardContent-root']"
    # reports_count_field_xpath = "//main/div[2]/div[3]/div"
    # scouts_panel_description_xpath = "//*[contains(@class, 'TextSecondary')]"
