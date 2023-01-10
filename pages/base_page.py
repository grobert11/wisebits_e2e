from selenium.webdriver.common.by import By


class BasePage:
    REQUEST_FIELD = (By.ID, 'textareaCodeSQL')
    BUTTON_RUN = (By.CSS_SELECTOR, "button.ws-btn")
    RESULT_MESSAGE = (By.ID, "divResultSQL")

    RESULT_TABLE = (By.CSS_SELECTOR, "table.ws-table-all")
    TABLE_ROW = (By.CSS_SELECTOR, "table.ws-table-all tr")
    TABLE_COLUMN_VALUE = (By.CSS_SELECTOR, "td")
    TABLE_COLUMNS_NAME = (By.CSS_SELECTOR, "table.ws-table-all tr:nth-child(1)")


    def button_click(self, browser) -> None:
        button_run = browser.find_element(*BasePage.BUTTON_RUN)
        button_run.click()


    def send_query(self, browser, query) -> None:
        browser.execute_script(f"window.editor.doc.setValue('{query}')")
        button_run = browser.find_element(*BasePage.BUTTON_RUN)
        button_run.click()


