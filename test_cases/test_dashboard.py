from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test001Dashboard:
    base_url = ReadConfig.get_application_url()
    page_title = ReadConfig.get_page_title()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):

        self.logger.info("----------------------- Test001Dashboard --------------------")
        self.logger.info("****************** Verifying Home page Title ******************")

        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == self.page_title:
            assert True
            self.driver.close()
            self.logger.info("****************** Home page title Passed ******************")

        else:
            self.driver.save_screenshot('../screen_shots/test_homePageTitle.png')
            self.driver.close()
            self.logger.error("****************** Home Page title Failed ******************")
            assert False
