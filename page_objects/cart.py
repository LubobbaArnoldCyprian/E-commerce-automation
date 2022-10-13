# from typing import re
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import re


class Cart:
    button_women_category_xpath = "//a[@title='Women']"
    button_t_shirts_category_xpath = "//a[contains(.,'T-shirts')]"
    select_item_xpath = "//a[normalize-space()='Blouse']"
    add_to_cart_xpath = "//span[normalize-space()='Add to cart']"
    proceed_to_checkout_xpath = "//span[normalize-space()='Proceed to checkout']"
    icon_plus_xpath = "//i[@class='icon-plus']"

    unit_price_xpath = "//span[@id='our_price_display']"
    product_quantity_xpath = "//span[@class='heading-counter']"
    overall_total_xpath = "//td[@id='total_product']"
    view_shopping_cart_xpath = "//a[@title='View my shopping cart']"
    empty_shopping_cart_xpath = "//a[@title='remove this product from my cart']"

    def __init__(self, driver):
        self.driver = driver

    # TC5
    # in the loop below you increase the product to the count declared.
    def select_item(self):
        self.driver.find_element(By.XPATH, self.select_item_xpath).click()
        icon_add = self.driver.find_element(By.XPATH, self.icon_plus_xpath)
        count = 11
        while count > 1:
            icon_add.click()
            # do your verification
            count -= 1
        self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()

        # TC5
        # Calculating total of items (unit price * quantity)
    def calculate_total(self):
        original_unit_price = self.driver.find_element(By.XPATH, self.unit_price_xpath).text
        # int converts string to integer
        # re.sub is used to remove all non-numeric characters and only remain with characters in range of 1 and 9
        unit_price = int(re.sub(r'[^0-9]', '', original_unit_price))
        print(unit_price)
        time.sleep(3)

        self.driver.find_element(By.XPATH, self.proceed_to_checkout_xpath).click()
        time.sleep(5)

        original_quantity = self.driver.find_element(By.XPATH, self.product_quantity_xpath).text
        # original_quantity = self.driver.find_element(By.CSS_SELECTOR, self.quantity_ccs_selector).text
        quantity = int(re.sub(r'[^0-9]', '', original_quantity))
        # quantity = str(original_quantity)
        print(quantity)
        time.sleep(3)

        final_total = unit_price * quantity
        print(final_total)

        overall_total = self.driver.find_element(By.XPATH, self.overall_total_xpath).text
        # int converts string to integer
        # re.sub is used to remove all non-numeric characters and only remain with characters in range of 1 and 9
        real_total = int(re.sub(r'[^0-9]', '', overall_total))
        print(real_total)
        time.sleep(3)

        # verifying displayed total matches calculated total
        assert final_total == real_total, f"total doesn't match" \
                                          f"Actual:{final_total}" \
                                          f"Expected: {real_total}"

        view_cart = self.driver.find_element(By.XPATH, self.view_shopping_cart_xpath)
        action_chains1 = ActionChains(self.driver)
        action_chains1.move_to_element(view_cart)
        action_chains1.perform()
        time.sleep(4)

        empty_shopping_cart = self.driver.find_element(By.XPATH, self.empty_shopping_cart_xpath)
        empty_shopping_cart.click()
