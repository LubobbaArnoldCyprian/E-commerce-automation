from selenium.webdriver.common.by import By


class Signin:
    button_signin_xpath = "//a[normalize-space()='Sign in']"
    textbox_email_signin_xpath = "//input[@id='email']"
    textbox_password_signin_xpath = "//input[@id='passwd']"
    button_login_xpath = "//span[contains(.,'Sign in')]"

    def __init__(self, driver):
        self.driver = driver

    def click_signin_dashboard(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()

    def click_signin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def set_email(self, email):
        signin_email_field = self.driver.find_element(By.XPATH, self.textbox_email_signin_xpath)
        signin_email_field.clear()
        signin_email_field.send_keys(email)

    def set_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.textbox_password_signin_xpath)
        password_field.send_keys(password)
        password_field.click()
