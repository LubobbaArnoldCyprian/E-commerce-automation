from page_objects.signin import Signin
from utilities.read_properties import ReadConfig


class Test_002_signin:
    baseUrl = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_signin(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.si = Signin(self.driver)
        self.si.click_signin_dashboard()
        self.si.set_email(self.email)
        self.si.set_password(self.password)
        self.si.click_signin()
        self.driver.close()
