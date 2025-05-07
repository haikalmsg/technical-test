from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ImportPage:
    def __init__(self, driver):
        self.driver = driver
        self.import_input = (By.XPATH, "//input[@type='file']")
        self.submit_button = (By.XPATH, "//button[@type='submit' and contains(., 'Upload File') and .//i[contains(@class, 'mdi-content-save')]]")
        self.wrong_file_message = (By.XPATH, "//div[@class='alert alert-danger']")
        self.invalid_format_message = (By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The data format does not match']")

    def upload_file(self, file_path):
        self.driver.find_element(*self.import_input).send_keys(file_path)
        self.driver.implicitly_wait(10)
    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
        self.driver.implicitly_wait(10)