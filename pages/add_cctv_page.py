from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddCCTVPage:
    def __init__(self, driver):
        self.driver = driver
        self.submit_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary') and .//i[contains(@class, 'mdi-content-save')] and contains(text(), 'Save')]")
        self.work_unit_dropdown = (By.XPATH, "//span[@id='select2-work_unit-container']")
        self.work_unit_option_test1 = (By.XPATH, "//ul[@id='select2-work_unit-results']/li[text()='test1']")
        self.cctv_name_input = (By.XPATH, "//input[@id='name' and @name='name']")
        self.cctv_id = (By.XPATH, "//input[@id='cctv_id' and @name='cctv_id']")
        self.ip_address_input = (By.XPATH, "//input[@id='ip_address' and @name='ip_address']")
    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
        self.driver.implicitly_wait(10)
    def click_work_unit_dropdown(self):
        self.driver.find_element(*self.work_unit_dropdown).click()
        self.driver.implicitly_wait(10)
    def click_work_unit_option_test1(self):
        self.driver.find_element(*self.work_unit_option_test1).click()
        self.driver.implicitly_wait(10)
    def enter_cctv_name(self, term):
        self.driver.find_element(*self.cctv_name_input).send_keys(term)
        self.driver.implicitly_wait(10)
    def enter_cctv_id(self, term):
        self.driver.find_element(*self.cctv_id).send_keys(term)
        self.driver.implicitly_wait(10)
    def enter_ip_address(self, term):
        self.driver.find_element(*self.ip_address_input).send_keys(term)
        self.driver.implicitly_wait(10) 