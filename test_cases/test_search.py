from page_objects.search import Search
from utilities.read_properties import ReadConfig


class Test_003_search:
    baseUrl = ReadConfig.get_application_url()
    product_search = ReadConfig.get_product_search()
    product_search_criteria = ReadConfig.get_product_search_criteria()

# TC1
# The function below is for product search and verifying the first result matches the search criteria
    def test_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.i = Search(self.driver)
        self.i.set_search_parameter(self.product_search)
        self.i.click_submit_search()
        self.i.confirm_product_name()
        self.driver.close()

# TC2
# From an array, we use a loop to perform a search and verify the searched parameter
    def test_search_002(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.i = Search(self.driver)

        search_array = self.product_search_criteria.split(",")

        for i in range(len(search_array)):
            if i <= 0:
                self.i.set_search_criteria_parameter(search_array[0])
                self.i.click_submit_search()
                self.i.clear_search_field()
                self.i.confirm_product_name_blouse()

            elif i == 1:
                self.i.set_search_criteria_parameter(search_array[1])
                self.i.click_submit_search()
                self.i.clear_search_field()
                self.i.confirm_product_name_tshirts()

            elif i == 2:
                self.i.set_search_criteria_parameter(search_array[2])
                self.i.click_submit_search()
                self.i.clear_search_field()
                self.i.confirm_product_name_dresses()

# TC3
# use of data driven test to perform a product search. In this case we are picking data from an excel sheeet.
    def test_data_excel(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(6)
        self.driver.get(self.baseUrl)
        self.e = Search(self.driver)
        self.e.data_from_excel()
        self.driver.close()
