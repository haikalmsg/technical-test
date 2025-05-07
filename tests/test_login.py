import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_login_wrong(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    login_page.enter_email("haikalrasyad@gmail.com")
    login_page.enter_password("keren 123")
    login_page.click_login()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//li[text()='auth.failed']"))
    )
    error_msg = driver.find_element(By.XPATH, "//li[text()='auth.failed']")
    assert error_msg.is_displayed()
def test_login_success(driver):
    driver.get("https://dsh-poc.assistxvision.ai/")
    login_page = LoginPage(driver)
    login_page.enter_email("waniadmin@yopmail.com")
    login_page.enter_password("Password123@")
    login_page.click_login()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
         (By.XPATH, "//li[contains(@class, 'breadcrumb-item') and text()[normalize-space()='Dashboard']]")
        )
    )
    # Optional: confirm it's displayed
    breadcrumb = driver.find_element(By.XPATH, "//li[contains(@class, 'breadcrumb-item') and text()[normalize-space()='Dashboard']]")
    assert breadcrumb.is_displayed()


