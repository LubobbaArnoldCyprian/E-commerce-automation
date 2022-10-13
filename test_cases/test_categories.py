from selenium import webdriver
from page_objects.categories import *
from utilities.read_properties import ReadConfig


# TC6
# Hovering over a main category and selecting a subcategory

class Test_005_categories:
    baseUrl = ReadConfig.get_application_url()

    def test_categories(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(6)
        self.driver.get(self.baseUrl)
        self.cat = Category(self.driver)
        self.cat.click_women()
        self.driver.close()
