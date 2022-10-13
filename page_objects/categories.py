from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# TC6
class Category:
    button_women_category_xpath = "//a[@title='Women']"
    button_t_shirts_category_xpath = "//a[contains(.,'T-shirts')]"

    def __init__(self, driver):
        self.driver = driver

    def click_women(self):
        women_button = self.driver.find_element(By.XPATH, self.button_women_category_xpath)
        action_chains1 = ActionChains(self.driver)
        action_chains1.move_to_element(women_button)
        action_chains1.perform()
        self.driver.find_element(By.XPATH, self.button_t_shirts_category_xpath).click()
