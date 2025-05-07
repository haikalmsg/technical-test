import pytest
import os
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_cctv_page import AddCCTVPage
from pages.import_page import ImportPage
from pages.edit_cctv_page import EditCCTVPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_upload_file_wrong_format(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    import_page = ImportPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_master_data()
    dashboard_page.click_import()
    dashboard_page.click_browse()
    import_page.upload_file("/Users/haikalmuhammadzg/Downloads/Data Device.xlsx")
    import_page.click_submit()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The data format does not match']"))
    )
    error_msg = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The data format does not match']")
    time.sleep(2)
    assert error_msg.is_displayed()
def test_upload_correct_file(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    import_page = ImportPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_master_data()
    dashboard_page.click_import()
    dashboard_page.click_browse()
    import_page.upload_file("/Users/haikalmuhammadzg/Downloads/master_data.xlsx")
    import_page.click_submit()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success' and normalize-space(text())='Add Import Successfully']"))
    )
    success_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success' and normalize-space(text())='Add Import Successfully']")
    time.sleep(2)
    assert success_msg.is_displayed()