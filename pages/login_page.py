from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id= 'password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    login_url = 'https://scouts.futbolkolektyw.pl/en/'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    sign_in_button_text = "Sign in"
    language_xpath = "//*[@role='button']"
    dropdown_polski_xpath = "//li[@data-value='pl']"
    dropdown_english_xpath = "//li[@data-value='en']"
    expected_remind_page_header = "Remind password"
    invalid_login_message_xpath = "//span[contains(@class, 'MuiTypography-root')]"
    expected_invalid_password_message = "Identifier or password invalid."
    expected_empty_login_message = "Please provide your username or your e-mail."



    def type_in_login(self, login):
        self.field_send_keys(self.login_field_xpath, login)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_language_listbox(self):
        self.click_on_the_element(self.language_xpath)

    def log_in(self, login, password):
        self.type_in_login(login)
        self.type_in_password(password)
        self.click_on_the_sign_in_button()

    def select_language(self, language):
        self.click_on_the_element(self.language_xpath)
        if language == "Polski":
            self.click_on_the_element(self.dropdown_polski_xpath)
        else:
            self.click_on_the_element(self.dropdown_english_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def invalid_password_check_message(self):
        self.assert_element_text(self.driver, self.invalid_login_message_xpath, self.expected_invalid_password_message)

    def empty_login_check_message(self):
        self.assert_element_text(self.driver, self.invalid_login_message_xpath, self.expected_empty_login_message)

    def assert_sign_in_text(self):
        self.assert_element_text(self.driver, self.sign_in_button_xpath, self.sign_in_button_text)

    def check_title_of_box(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    # def get_element_text(self):
    #     self.driver.find_elements_by_xpath("//*[contains(text(), 'Sign in')]")