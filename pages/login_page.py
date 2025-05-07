from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.password_input = (By.NAME, "password")
        self.email_input = (By.NAME, "email")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, term):
        self.driver.find_element(*self.email_input).send_keys(term)

    def enter_password(self, term):
        self.driver.find_element(*self.password_input).send_keys(term)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        self.driver.implicitly_wait(30)