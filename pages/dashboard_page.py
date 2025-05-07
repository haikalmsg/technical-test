from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DashboardPage:
      def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.CSS_SELECTOR, "button[data-bs-original-title='Logout']")
        self.reliability_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/realibility']")
        self.alerts_button = (By.CSS_SELECTOR, "a[href='#dashboardsExamples']")
        self.intrusion_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/intrusion']")
        self.download_button = (By.XPATH, "//span[i[@class='fa fa-file-excel'] and contains(text(), 'Export Excel')]")
        self.master_data_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/master_data']")
        self.import_button = (By.XPATH, "//button[contains(@class, 'btn-import-primary') and .//i[contains(@class, 'fa-file-import')]]")
        self.browse_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/master_data/import_file']")
        self.cctv_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/cctv']")
        self.add_data_button = (By.CSS_SELECTOR, "a[href='https://dsh-poc.assistxvision.ai/cctv/create']")
        self.delete_cctv_button_1 = (By.XPATH, "//a[contains(@class, 'btnDelete') and @title='Delete Data']")
        self.confirm_delete_button = (By.ID, "btnDeleteConfirm")
        self.cancel_delete_button = (By.XPATH, "//button[contains(@class,'btn-secondary') and @data-bs-dismiss='modal' and normalize-space()='Cancel']")
        self.edit_cctv_button = (By.XPATH, "//a[@title='Edit Data' and contains(@class, 'btn-warning')]")
      def click_logout(self):
         self.driver.find_element(*self.logout_button).click()
         self.driver.implicitly_wait(10)
      def click_reliability(self):
         self.driver.find_element(*self.reliability_button).click()
         self.driver.implicitly_wait(10)
      def click_alerts(self):
         self.driver.find_element(*self.alerts_button).click()
         self.driver.implicitly_wait(10)
      def click_intrusion(self):
         self.driver.find_element(*self.intrusion_button).click()
         self.driver.implicitly_wait(10)
      def click_download(self):
         self.driver.find_element(*self.download_button).click()
         self.driver.implicitly_wait(10)
      def click_master_data(self):
         self.driver.find_element(*self.master_data_button).click()
         self.driver.implicitly_wait(10)
      def click_import(self):
         self.driver.find_element(*self.import_button).click()
         self.driver.implicitly_wait(10)
      def click_browse(self):
         self.driver.find_element(*self.browse_button).click()
         self.driver.implicitly_wait(10)
      def click_cctv(self):
         self.driver.find_element(*self.cctv_button).click()
         self.driver.implicitly_wait(10)
      def click_add_data(self):
         self.driver.find_element(*self.add_data_button).click()
         self.driver.implicitly_wait(10)
      def click_delete_cctv(self):
         self.driver.find_element(*self.delete_cctv_button_1).click()
         self.driver.implicitly_wait(10)
      def click_confirm_delete(self):
         self.driver.find_element(*self.confirm_delete_button).click()
         self.driver.implicitly_wait(10)
      def click_cancel_delete(self):
          from selenium.webdriver.support.ui import WebDriverWait
          from selenium.webdriver.support import expected_conditions as EC
          from selenium.webdriver.common.by import By

          # Wait until the cancel button is clickable, then click
          WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable(self.cancel_delete_button)
          )
          self.driver.find_element(*self.cancel_delete_button).click()
      def click_edit_cctv(self):
         self.driver.find_element(*self.edit_cctv_button).click()
         self.driver.implicitly_wait(10)