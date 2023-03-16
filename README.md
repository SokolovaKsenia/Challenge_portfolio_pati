<img src="https://github.com/SokolovaKsenia/challenge_portfolio_KS/blob/main/images/readme-banner.jpg"/>

<p style="text-align: center;"><em>Below is the implementation of the <strong>second task</strong> of the Challenge - finding selectors for the elements on the login page &dArr;&dArr;&dArr;</em></p>
<hr />
<p></p>

<h1 style="text-align: center; color:#00BFFF">TASK 2: Selectors</h1>


## Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page. ##

**login_field_xpath** 
1. //*[@id="login"]
2. //*[@name="login"]
3. //*[@type="text"]

**password_field_xpath** 
1. //*[@id='password']
2. //*[@name="password]
3. //*[@type="password"]

**sign_in_button_xpath**
1. //*[text()="Sign in"]
2. //*[@class = "MuiButton-label"]
3. //*[@type="submit"]/span[2]

**remind_password_xpath**
1. //*[@id="__next"]/form/div/div[1]/a
2. //*[text()="Remind password"]
3. //child::div/a

**language_xpath**
1. //*[@role="button"]
2. //*[@tabindex="0"]
3. //*[@aria-haspopup="listbox"]

**language_dropdown_polski_xpath**
1. //*[text()="Polski"]
2. //*[@role= "option" and text()= "Polski"]
3. //*[@id="menu-"]/div[3]/ul/li[1]

**language_dropdown_english_xpath**
1. //*[text()="English"]
2. //*[@id="menu-"]/div[3]/ul/li[2]
3. //*[@role= "option" and text()= "English"]

**scout_panel_heading_xpath**
1. //*[text()="Scouts Panel"]
2. //*[contains(@class, "MuiTypography-h5")]
3. //h5

**zaloguj_xpath**
1. //button[@type= "submit"]
2. //*[contains(@class, "MuiButtonBase")]
3. //button[@tabindex= "0"]






