from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils import wait_element, get_rows_list_of_resulted_table, get_resulted_dicts_in_list


base_page = BasePage()


def test_get_all_rows_and_check_certain_row(browser) -> None:
    test_data = {
        'ContactName': 'Giovanni Rovelli',
         'Adress': 'Via Ludovico il Moro 22'
                  }

    wait_element(base_page.BUTTON_RUN, browser)
    base_page.button_click(browser)

    wait_element(base_page.RESULT_TABLE, browser)

    for row in get_resulted_dicts_in_list(browser):
        if test_data['ContactName'] in row:
            assert test_data['Address'] == row['Address']


def test_get_rows_where_city_is_london(browser) -> None:
    test_data = {
        'City': 'London',
    }
    wait_element(base_page.REQUEST_FIELD, browser)

    test_query = f'SELECT * FROM Customers WHERE City="{test_data["City"]}";'
    base_page.send_query(browser, test_query)
    wait_element(base_page.RESULT_TABLE, browser)
    assert len(get_rows_list_of_resulted_table(browser)) == 6



def test_add_new_row_into_table(browser) -> None:
    test_data = {
        'CustomerID': '92',
        'CustomerName': 'Robert',
        'ContactName': 'Roberto',
        'Address': 'Kremlin',
        'City': 'Moscow',
        'PostalCode': '4321',
        'Country': 'Russia'
    }
    wait_element(base_page.REQUEST_FIELD, browser)

    keys =','.join([keys for keys in test_data.keys()])
    val = '","'.join([val for val in test_data.values()])

    query = f'INSERT INTO Customers ({keys}) VALUES ("{val}")'
    base_page.send_query(browser, query)
    result = (By.ID, 'divResultSQL')
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(result, 'You have made changes to the database. Rows affected: 1'))


    base_page.send_query(browser, f"SELECT * FROM Customers where CustomerID = {test_data['CustomerID']};")
    wait_element(base_page.RESULT_TABLE, browser)
    result = get_resulted_dicts_in_list(browser)
    assert result[0] == test_data


def test_update_row_in_table(browser) -> None:
    test_data = {
        'CustomerName': 'Robert',
        'ContactName': 'Roberto',
        'Address': 'Kremlin',
        'City': 'Moscow',
        'PostalCode': '4321',
        'Country': 'Russia'
    }
    val = ",".join([k + f' ="{v}"' for k, v in test_data.items()])
    query = f'Update Customers Set {val} Where CustomerID=5'

    test_data.update({'CustomerID':'5'})
    base_page.send_query(browser, query)

    base_page.send_query(browser, f"SELECT * FROM Customers where CustomerID = 5;")
    wait_element(base_page.RESULT_TABLE, browser)
    result = get_resulted_dicts_in_list(browser)
    assert result[0] == test_data


def test_delete_row_from_table(browser) -> None:
    test_data = {
        "CustomerID": "2"
    }
    query = f'Delete from Customers where CustomerID=2'
    base_page.send_query(browser, query)
    wait_element(base_page.RESULT_MESSAGE, browser)
    base_page.send_query(browser, "SELECT CustomerID FROM Customers")
    wait_element(base_page.RESULT_TABLE, browser)
    result = get_resulted_dicts_in_list(browser)
    for rows in result:
        assert test_data['CustomerID'] not in rows



