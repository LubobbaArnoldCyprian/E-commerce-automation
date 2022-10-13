from page_objects.cart import Cart
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.read_properties import ReadConfig
import time


class Test_006_cart:
    baseUrl = ReadConfig.get_application_url()
    unit_price_blouse = ReadConfig.get_unit_price()

    def test_cart(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(7)
        self.driver.get(self.baseUrl)
        self.cart = Cart(self.driver)
        self.driver.execute_script("window.scrollBy(0,500)", "")
        self.cart.select_item()
        time.sleep(5)
        self.cart.calculate_total()
        time.sleep(10)

        self.driver.close()
