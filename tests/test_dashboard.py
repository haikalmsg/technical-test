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

def test_logout(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_logout()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    inputs = driver.find_element(By.NAME, "email")
    assert inputs.is_displayed()

def test_click_tabs(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_reliability()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Reliability']"))
    )
    reliability_header = driver.find_element(By.XPATH, "//h4[text()='Reliability']")
    assert reliability_header.is_displayed()
def test_download(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_alerts()
    dashboard_page.click_intrusion()
    dashboard_page.click_download()
    time.sleep(5)  # wait for download to complete

    download_dir = "/Users/haikalmuhammadzg/Downloads"
    file_path = os.path.join(download_dir, "Data Alert Intrusion.xlsx")
    assert os.path.exists(file_path), "Downloaded file not found"
   

