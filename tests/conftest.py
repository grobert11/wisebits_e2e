import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@pytest.fixture(autouse=True)
def reset_db(browser):
    RESET_BUTTON = (By.ID, 'restoreDBBtn')
    result = (By.ID, 'divResultSQL')
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(RESET_BUTTON))
        browser.find_element(By.ID, 'restoreDBBtn').click()

        WebDriverWait(browser, 10).until(EC.alert_is_present())
        browser.switch_to.alert.accept()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(result, 'The database is fully restored.'))
    except (NoSuchElementException, TimeoutException):
        browser.refresh()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(RESET_BUTTON))
        browser.find_element_by_id(By.ID, 'restoreDBBtn').click()

        WebDriverWait(browser, 10).until(EC.alert_is_present())
        browser.switch_to.alert.accept()
        browser.find_element(By.ID, 'divResultSQL')