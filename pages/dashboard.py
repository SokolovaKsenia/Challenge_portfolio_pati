from pages.base_page import BasePage


class Dashboard(BasePage):

    dev_team_contact_hyperlink_xpath = "// a[contains(@ href, '://')]"
    logo_scouts_panel_xpath = "//*[contains(@class, "MuiCardMedia")]"
    add_player_hyperlink_xpath = "//*[2][name()="a"]"
    super_man_hyperlink_xpath = "//h6//following-sibling::a[1]"
    scouts_panel_xpath = "//*[contains(@class, "MuiTypography-root MuiTypography")]"
    scouts_panel_header_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
    main_page_icon_xpath = "//*[contains(@class, "MuiSvgIcon-root jss23 jss24")]"
    main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]"
    main_page_xpath = "//*[contains(@class, "MuiTypography-root MuiListItemText")]"
    players_icon_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[1]/svg/path"
    polski_button_xpath = "//*[text()="Polski"]"
    matches_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[1]"
    scouts_panel_block_xpath = "//*[contains(@class, "MuiCardContent - root")]"
    leftsidebar_xpath = "//*[contains(@class, "MuiDrawer-paperAnchorDockedLeft")]"
    header_xpath = "//*[@id="__next"]/div[1]/header/div"
    sign_out_button_xpath = "//*[contains(@class, "MuiListItem-button")]"
    players_count_field_xpath = "//*[contains(@class, "MuiGrid-grid-md")]"
    last_created_player_xpath = "//h6"
    shortcuts_block_xpath = "//*[contains(@class, "MuiCardContent-root")]"
    reports_count_field_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[3]/div"
    scouts_panel_description_xpath = "//*[contains(@class, "MuiTypography-body2")]"

    pass

