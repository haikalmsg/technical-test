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

def test_edit(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    edit_cctv_page = EditCCTVPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_edit_cctv()
    time.sleep(2)
    expected_values = {
        "work_unit": "test1",
        "cctv_name": "akjdajdn",
        "cctv_id": "ajkdnajdbajkd",
        "ip_address": "123.91.29.31"
    }
    edit_cctv_page.assert_input_values(expected_values)

def test_add_cctv_invalid_input(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    add_cctv_page = AddCCTVPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_add_data()
    add_cctv_page.enter_cctv_id("a")
    add_cctv_page.enter_cctv_name("a")
    add_cctv_page.enter_ip_address(1)
    add_cctv_page.click_submit()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The work unit is required']"))
    )
    work_unit_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The work unit is required']")
    assert work_unit_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The name min 3 characters']"))
    )
    name_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The name min 3 characters']")
    assert name_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The cctv id min 3 characters']"))
    )
    id_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The cctv id min 3 characters']")
    assert id_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='validation.ipv4']"))
    )
    ip_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='validation.ipv4']")
    assert ip_error.is_displayed()

def test_add_cctv_no_input(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    add_cctv_page = AddCCTVPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_add_data()
    add_cctv_page.click_submit()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The work unit is required']"))
    )
    work_unit_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The work unit is required']")
    assert work_unit_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The name is required']"))
    )
    name_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The name is required']")
    assert name_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The cctv id is required']"))
    )
    id_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The cctv id is required']")
    assert id_error.is_displayed()

    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The IP address is required']"))
    )
    ip_error = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[text()='The IP address is required']")
    assert ip_error.is_displayed()
def test_add_cctv_valid_input(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    add_cctv_page = AddCCTVPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_add_data()
    add_cctv_page.click_work_unit_dropdown()
    add_cctv_page.click_work_unit_option_test1()
    add_cctv_page.enter_cctv_name("test")
    add_cctv_page.enter_cctv_id("xxxxxxx")
    add_cctv_page.enter_ip_address("192.168.1.1")
    add_cctv_page.click_submit()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success' and normalize-space()='Add data successfully']"))
    )
    success_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success' and normalize-space()='Add data successfully']")
    assert success_msg.is_displayed()
def test_add_cctv_duplicate(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    add_cctv_page = AddCCTVPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_add_data()
    add_cctv_page.click_work_unit_dropdown()
    add_cctv_page.click_work_unit_option_test1()
    add_cctv_page.enter_cctv_name("test")
    add_cctv_page.enter_cctv_id("test")
    add_cctv_page.enter_ip_address("192.168.1.1")
    add_cctv_page.click_submit()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[normalize-space()='The cctv id already exists']"))
    )
    duplciate_err = driver.find_element(By.XPATH, "//span[@class='invalid-feedback' and @role='alert']/strong[normalize-space()='The cctv id already exists']")
    assert duplciate_err.is_displayed()
def test_delete_cctv(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_delete_cctv()
    dashboard_page.click_confirm_delete()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success d-flex align-items-center' and @role='alert']/div[normalize-space()='Success Delete Data!']"))
    )
    success_msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success d-flex align-items-center' and @role='alert']/div[normalize-space()='Success Delete Data!']")
    assert success_msg.is_displayed()
def test_cancel_delete_cctv(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    dashboard_page.click_cctv()
    dashboard_page.click_delete_cctv()
    dashboard_page.click_cancel_delete()
    webdriver_wait = WebDriverWait(driver, 10)
    webdriver_wait.until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@class='modal-content']//h4[normalize-space()='Are you sure?']"))
    )
    cancel_msg = driver.find_element(By.XPATH, "//div[@class='modal-content']//h4[normalize-space()='Are you sure?']")
    assert not cancel_msg.is_displayed()
