from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support.ui import Select


class SignUp:
    textbox_email_xpath = "//input[@id='email_create']"
    button_create_account_xpath = "//span[normalize-space()='Create an account']"
    button_signin_dashboard_xpath = "//a[normalize-space()='Sign in']"
    button_female_gender_xpath = "//input[contains(@id,'id_gender1')]"
    button_male_gender_xpath = ""
    textbox_fname_xpath = "//input[@id='customer_firstname']"
    textbox_lname_xpath = "//input[@id='customer_lastname']"
    textbox_password_xpath = "//input[@id='passwd']"
    drop_down_day_DOB_xpath = "//select[@id='days']"
    drop_down_month_DOB_xpath = "//select[@id='months']"
    drop_down_year_DOB_xpath = "//select[@id='years']"
    textbox_address_fname_xpath = "//input[@id='passwd']"
    textbox_address_lname_xpath = "//input[@id='lastname']"
    textbox_company_xpath = "//input[@id='company']"
    textbox_address_xpath = "//input[@name='address1']"
    textbox_city_xpath = "//input[@id='city']"
    drop_down_state_xpath = "//select[@id='id_state']"
    text_postal_code_xpath = "//input[@id='postcode']"
    textbox_mobile_phone_xpath = "//input[@id='phone_mobile']"
    textbox_address_reference_xpath = "//input[@id='alias']"
    button_register_xpath = "//span[normalize-space()='Register']"

    def __init__(self, driver):
        self.driver = driver

    def click_signin_dashboard(self):
        self.driver.find_element(By.XPATH, self.button_signin_dashboard_xpath).click()

    def set_user_email(self, email):

        signup_email_field = self.driver.find_element(By.XPATH, self.textbox_email_xpath)
        signup_email_field.clear()
        signup_email_field.send_keys(email)

    def click_create_account(self):
        self.driver.find_element(By.XPATH, self.button_create_account_xpath).click()

    def set_first_name(self, first_name):
        firstname_field = self.driver.find_element(By.XPATH, self.textbox_fname_xpath)
        firstname_field.clear()
        firstname_field.send_keys(first_name)

    def set_last_name(self, last_name):
        lastname_field = self.driver.find_element(By.XPATH, self.textbox_lname_xpath)
        lastname_field.clear()
        lastname_field.send_keys(last_name)

    def set_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        password_field.send_keys(password)
        password_field.click()

    def set_address_first_name(self, address_first_name):
        address_first_name_field = self.driver.find_element(By.XPATH, self.textbox_address_fname_xpath)
        address_first_name_field.clear()
        address_first_name_field.send_keys(address_first_name)

    def set_address_last_name(self, address_last_name):
        address_last_name_field = self.driver.find_element(By.XPATH, self.textbox_address_lname_xpath)
        address_last_name_field.click()
        address_last_name_field.send_keys(address_last_name)

    def set_company(self, company):
        company_field = self.driver.find_element(By.XPATH, self.textbox_company_xpath)
        company_field.clear()
        company_field.send_keys(company)

    def set_address(self, address):
        address_field = self.driver.find_element(By.XPATH, self.textbox_address_xpath)
        address_field.clear()
        address_field.send_keys(address)

    def set_city(self, city):
        city_field = self.driver.find_element(By.XPATH, self.textbox_city_xpath)
        city_field.clear()
        city_field.send_keys(city)

    def set_postal_code(self, postal_code):
        postal_code_field = self.driver.find_element(By.XPATH, self.text_postal_code_xpath)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def set_mobile_phone(self, mobile_phone):
        mobile_phone_field = self.driver.find_element(By.XPATH, self.textbox_mobile_phone_xpath)
        mobile_phone_field.clear()
        mobile_phone_field.send_keys(mobile_phone)

    def set_address_reference(self, address_reference):
        address_reference_field = self.driver.find_element(By.XPATH, self.textbox_address_reference_xpath)
        address_reference_field.clear()
        address_reference_field.send_keys(address_reference)

    def set_dob_day(self, day_DOB):
        day_DOB_field = Select(self.driver.find_element(By.XPATH, self.drop_down_day_DOB_xpath))

        day_DOB_field.select_by_value(day_DOB)

    def set_dob_month(self, month_DOB):
        day_DOB_field = Select(self.driver.find_element(By.XPATH, self.drop_down_month_DOB_xpath))
        day_DOB_field.select_by_value(month_DOB)

    def set_dob_year(self, year_DOB):
        day_DOB_field = Select(self.driver.find_element(By.XPATH, self.drop_down_year_DOB_xpath))
        day_DOB_field.select_by_value(year_DOB)

    def set_state(self, state):
        state_field = Select(self.driver.find_element(By.XPATH, self.drop_down_state_xpath))
        state_field.select_by_visible_text(state)

    def click_register(self):
        self.driver.find_element(By.XPATH, self.button_register_xpath).click()

















