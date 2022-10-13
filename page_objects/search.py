from selenium.webdriver.common.by import By
import openpyxl as O
from utilities.XLUtils import ws


class Search:
    textbox_search_xpath = "//input[@id='search_query_top']"
    button_submit_search_xpath = "//button[@name='submit_search']"
    confirm_product_name_xpath = "//a[@title='Blouse'][normalize-space()='Blouse']"
    confirm_product_name_universal_xpath = "//span[@class='lighter']"

    product_blouse = '"BLOUSE"'
    product_tshirts = '"T-SHIRTS"'
    product_dresses = '"DRESSES"'

    def __init__(self, driver):
        self.driver = driver
# TC1
# The function below is for product search and verifying the first result matches the search criteria

    def set_search_parameter(self, product_search):
        search_parameter_field = self.driver.find_element(By.XPATH, self.textbox_search_xpath)
        search_parameter_field.click()
        search_parameter_field.send_keys(product_search)

    def click_submit_search(self):
        self.driver.find_element(By.XPATH, self.button_submit_search_xpath).click()

    def confirm_product_name(self):
        confirm_product_name_field = self.driver.find_element(By.XPATH, self.confirm_product_name_xpath)
        msg_text = confirm_product_name_field.text
        print(msg_text)

        assert msg_text == "Blouse", f"not expected" \
                                     f"Actual:{msg_text}" \
                                     f"Expected: 'Blouse'"

# TC3
# use of data driven test to perform a product search. In this case we are picking data from an excel sheeet.
    def data_from_excel(self):
        textbox_search = self.driver.find_element(By.XPATH, self.textbox_search_xpath)
        for r in range(2, ws.max_row + 1):
            d = str(ws.cell(r, 1).value)
            textbox_search.clear()
            textbox_search.send_keys(d)
        button_submit_search = self.driver.find_element(By.XPATH, self.button_submit_search_xpath)
        button_submit_search.click()

        confirm_product_name_field = self.driver.find_element(By.XPATH, self.confirm_product_name_xpath)
        msg_text = confirm_product_name_field.text
        print(msg_text)

        assert msg_text == "Blouse", f"not expected" \
                                     f"Actual:{msg_text}" \
                                     f"Expected: 'Blouse'"

    # TC2
    # From an array, we use a loop to perform a search and verify the searched parameter
    def set_search_criteria_parameter(self, product_search_criteria):
        search_parameter_field = self.driver.find_element(By.XPATH, self.textbox_search_xpath)
        search_parameter_field.click()
        search_parameter_field.send_keys(product_search_criteria)

    def confirm_product_name_blouse(self):
        confirm_product_name_field = self.driver.find_element(By.XPATH, self.confirm_product_name_universal_xpath)
        msg_text = confirm_product_name_field.text
        print(msg_text)

        assert msg_text == self.product_blouse, f"not expected" \
                                                f"Actual:{msg_text}" \
                                                f"Expected: 'BLOUSE'"

    def confirm_product_name_tshirts(self):
        confirm_product_name_field = self.driver.find_element(By.XPATH, self.confirm_product_name_universal_xpath)
        msg_text = confirm_product_name_field.text
        print(msg_text)

        assert msg_text == self.product_tshirts, f"not expected" \
                                                 f"Actual:{msg_text}" \
                                                 f"Expected: 'T-SHIRTS'"

    def confirm_product_name_dresses(self):
        confirm_product_name_field = self.driver.find_element(By.XPATH, self.confirm_product_name_universal_xpath)
        msg_text = confirm_product_name_field.text
        print(msg_text)

        assert msg_text == self.product_dresses, f"not expected" \
                                                 f"Actual:{msg_text}" \
                                                 f"Expected: 'DRESSES'"

    def clear_search_field(self):
        search_parameter_field = self.driver.find_element(By.XPATH, self.textbox_search_xpath)
        search_parameter_field.clear()
