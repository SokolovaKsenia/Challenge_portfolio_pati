<img src="https://github.com/SokolovaKsenia/challenge_portfolio_KS/blob/main/images/readme-banner.jpg"/>

<h2 align="left">Hi there, I'm <a href="www.linkedin.com/in/kseniia-sokolova-ks">Kseniia</a> 
<img src="https://github.com/SokolovaKsenia/challenge_portfolio_KS/blob/main/images/Hi.gif.crdownload" height="32"/></h2>

<p></p>
<table style="width: 100%; border-collapse: collapse; border-style: inset; margin-left: auto; margin-right: auto;" cellpadding="20">
<tbody>
<tr>
<td style="width: 50%;">
<h3 style="text-align: center;"><span>Why did I choose to participate in the "Challenge portfolio project?</span></h3>
<p style="text-align: justify;">As the world of computer technology is developing very quickly, some time ago I've decided to immerse myself in the world of IT.</p>
<p style="text-align: justify;">Having behind my back over 15 years of experience in the field of social communications, I had finished<span>&nbsp;</span><strong>FrontEnd</strong><span>&nbsp;</span>development course first, and the whole last year I've devoted myself to<span>&nbsp;</span><strong>Manual QA</strong><span>&nbsp;</span>and<span>&nbsp;</span><strong>AQA</strong>: having studied on my own, finished several online courses (GoIT, EPAM) as well as taken internships at Ukrainian IT companies.</p>
<p style="text-align: justify;">From the project I expect to gain new knowledge, skills and opportunities. The best ever goal for me - is to get a new interesting job in this area.</p>
<blockquote>
<h4 style="text-align: center;"><span style="text-align: justify;"><span style="text-decoration: underline;"><em><strong>Thank you a lot for the chance to participate in Challenge Portfolio Program! :)</strong></em></span></span></h4>
</blockquote>
</td>
<td style="width: 50%; text-align: center; vertical-align: top;">
<h3><span>Dlaczego zdecydowałam się na udział w "Challenge portfolio"?</span></h3>
<p style="text-align: justify;">Ponieważ świat technologii komputerowej rozwija się bardzo szybko, jakiś czas temu postanowiłam zanurzyć się w świat technologij informatycznych.</p>
<p style="text-align: justify;">Już wcześniej uczyłam się programowania<strong><span>&nbsp;</span>FrontEnd</strong>, a w zeszłym roku poświęciłam sw&oacute;j czas<span>&nbsp;</span><strong>Manualną QA</strong><span>&nbsp;</span>i<span>&nbsp;</span><strong>AQA</strong>, ucząc się samodzielnie i odbywając staże w ukraińskich firmach IT.</p>
<p style="text-align: justify;">Od projektu oczekuję zdobycia nowej wiedzy oraz umiejętności. Pożądanym celem dla mnie jest r&oacute;wnież zdobycie nowej ciekawej pracy w tej dziedzinie.</p>
<blockquote>
<h4><span style="text-decoration: underline;"><strong><em>Dziękuję bardzo za możliwość uczestniczenia w tym projekcie! :)</em></strong></span></h4>
</blockquote>
</td>
</tr>
</tbody>
</table>
<p></p>
<p></p>
<hr />
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






