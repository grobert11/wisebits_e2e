from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage


def wait_element(locator, browser) -> None:
    """Element waiter"""
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))
    except (NoSuchElementException, TimeoutException):
        browser.refresh()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))


def get_rows_list_of_resulted_table(browser) -> list:
    """getting all rows from table and setting as list element"""
    result = []
    rows = browser.find_elements(*BasePage.TABLE_ROW)
    for row in rows[1:]:
        result.append([column.text for column in row.find_elements(*BasePage.TABLE_COLUMN_VALUE)])
    return result


def get_resulted_dicts_in_list(browser) -> list:
    """creating dict with column name as key and rows values as column values and putting into list
        eg. [{'CustomerID' : '1' ...}]"""
    get_column_list = browser.find_element(*BasePage.TABLE_COLUMNS_NAME).text.split()
    result = []
    resulted_rows = get_rows_list_of_resulted_table(browser)
    for row in resulted_rows:
        temp_dict = {}
        for i in range(len(row)):
            temp_dict[get_column_list[i]] = row[i]
        result.append(temp_dict)
    return result