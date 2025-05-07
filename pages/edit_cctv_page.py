from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class EditCCTVPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.save_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary') and .//i[contains(@class, 'mdi-content-save')] and normalize-space()='Save']")
        self.cctv_name_input = (By.XPATH, "//input[@id='name' and @name='name']")
        self.cctv_id = (By.XPATH, "//input[@id='cctv_id' and @name='cctv_id']")
        self.ip_address_input = (By.XPATH, "//input[@id='ip_address' and @name='ip_address']")
        self.work_unit_dropdown = (By.XPATH, "//span[@id='select2-work_unit-container']")

    def get_input_values(self):
        return {
            "cctv_name": self.driver.find_element(*self.cctv_name_input).get_attribute("value"),
            "cctv_id": self.driver.find_element(*self.cctv_id).get_attribute("value"),
            "ip_address": self.driver.find_element(*self.ip_address_input).get_attribute("value"),
            "work_unit": self.driver.find_element(*self.work_unit_dropdown).get_attribute("title"),
        }
    def assert_input_values(self, expected_values: dict):
        actual_values = self.get_input_values()
        for key, expected in expected_values.items():
            actual = actual_values.get(key)
            assert actual == expected, f"Expected {key} to be '{expected}', but got '{actual}'"