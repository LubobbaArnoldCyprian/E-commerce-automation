from page_objects.signup import SignUp
from utilities.read_properties import ReadConfig
import time


class Test_001_signup:
    baseUrl = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    first_name = ReadConfig.get_first_name()
    last_name = ReadConfig.get_last_name()
    password = ReadConfig.get_password()
    address_first_name = ReadConfig.get_address_first_name()
    address_last_name = ReadConfig.get_address_last_name()
    company = ReadConfig.get_company()
    address = ReadConfig.get_address()
    city = ReadConfig.get_city()
    postal_code = ReadConfig.get_postal_code()
    mobile_phone = ReadConfig.get_mobile()
    address_reference = ReadConfig.get_address_reference()
    day_DOB = ReadConfig.get_day_DOB()
    month_DOB = ReadConfig.get_month_DOB()
    year_DOB = ReadConfig.get_year_DOB()
    state = ReadConfig.get_state()

    def test_signup(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.su = SignUp(self.driver)
        self.su.click_signin_dashboard()
        self.su.set_user_email(self.email)
        self.su.click_create_account()
        self.su.set_first_name(self.first_name)
        self.su.set_last_name(self.last_name)
        self.su.set_dob_day(self.day_DOB)
        self.su.set_dob_month(self.month_DOB)
        self.su.set_dob_year(self.year_DOB)
        self.su.set_address_first_name(self.address_first_name)
        self.su.set_address_last_name(self.address_last_name)
        self.su.set_company(self.company)
        self.su.set_address(self.address)
        self.su.set_city(self.city)
        self.su.set_postal_code(self.postal_code)
        self.su.set_mobile_phone(self.mobile_phone)
        self.su.set_address_reference(self.address_reference)
        self.su.set_password(self.password)
        self.su.set_state(self.state)
        self.su.click_register()

        self.driver.quit()













