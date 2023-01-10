import pytest
from selenium import webdriver



@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    driver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
    yield driver
    driver.quit()




