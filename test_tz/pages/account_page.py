from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure

from .base_page import BasePage
from .locators import AccountPageLocators

TIME_WAIT_LONG = 3
TIME_WAIT_SHORT = 1


class AccountPage(BasePage):

    @allure.step("Нажатие на кнопку 'Deposit'")
    def click_on_deposit_button(self):
        deposit_button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.DEPOSIT_BUTTON))
        deposit_button.click()

    @allure.step("Введение суммы в поле ввода 'Amount to be Deposited'")
    def set_deposit_amount(self, amount: int):
        input_amount = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.presence_of_element_located(AccountPageLocators.AMOUNT_TO_BE_DEPOSITED_INPUT))
        input_amount.send_keys(amount)

    @allure.step("Нажатие на кнопку 'Deposit' внизу формы")
    def click_on_deposit_button_confirm(self):
        deposit_button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.DEPOSIT_BUTTON_CONFIRM))
        deposit_button.click()

    @allure.step("Проверка появления красной надписи 'Deposit Successful'")
    def check_deposit_successful_message(self):
        return self.is_element_present(*AccountPageLocators.DEPOSIT_SUCCESSSFUL_SPAN)

    @allure.step("Нажатие на кнопку 'Withdrawl'")
    def make_withdrawl_transaction(self, amount: int):
        self.click_on_withdrawl_button()
        self.set_withdrawl_amount(amount)
        self.click_on_withdrawl_button_confirm()

    @allure.step("Нажатие на кнопку 'Withdrawl'")
    def click_on_withdrawl_button(self):
        withdrawl_button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.WITHDRAWL_BUTTON))
        withdrawl_button.click()

    @allure.step("Введение суммы в поле ввода 'Amount to be Withdrawn'")
    def set_withdrawl_amount(self, amount: float):
        WebDriverWait(self.browser, TIME_WAIT_LONG).until(EC.element_to_be_clickable(AccountPageLocators.AMOUNT_TO_BE_WITHDRAWL_LABEL))
        input_amount = WebDriverWait(self.browser, TIME_WAIT_LONG).until(
            EC.element_to_be_clickable(AccountPageLocators.AMOUNT_TO_BE_WITHDRAWL_INPUT))
        input_amount.send_keys(amount)

    @allure.step("Нажатие на кнопку 'Withdrawn' внизу формы")
    def click_on_withdrawl_button_confirm(self):
        withdrawl_button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.WITHDRAWL_BUTTON_CONFIRM))
        withdrawl_button.click()

    @allure.step("Проверка появления красной надписи 'Transaction successful'")
    def check_withdrawl_successful_message(self):
        WebDriverWait(self.browser, TIME_WAIT_LONG). \
            until(EC.presence_of_element_located(AccountPageLocators.WITHDRAWL_BUTTON_CONFIRM))
        return self.is_element_present(*AccountPageLocators.WITHDRAWL_SUCCESSSFUL_SPAN)

    @allure.step("Считывание значения 'Balance'")
    def get_balance(self):
        balance_strong = WebDriverWait(self.browser, TIME_WAIT_LONG). \
            until(EC.presence_of_element_located(AccountPageLocators.BALANCE_LABEL))

        return int(balance_strong.text)

    @allure.step("Нажатие на кнопку 'Transaction'")
    def click_on_transactions_button(self):
        transactions_button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.TRANSACTIONS_BUTTON))
        transactions_button.click()

    @allure.step("Нажатие на кнопку 'Back'")
    def click_on_back(self):
        button = WebDriverWait(self.browser, TIME_WAIT_LONG).\
            until(EC.element_to_be_clickable(AccountPageLocators.BACK_BUTTON))
        button.click()

    @allure.step("Обнуление миллисекунд в левом поле Дата/время на странице 'Transactions'")
    def set_start_datetime_v2(self):
        datetime_box = WebDriverWait(self.browser, TIME_WAIT_LONG). \
            until(EC.element_to_be_clickable(AccountPageLocators.START_BUTTON))
        min_value = datetime_box.get_attribute('min')

        # date = min_value[5:7] + min_value[8:10] + min_value[0:4]
        time_ = min_value[11:13] + min_value[14:16] + min_value[17:19] + ",000"
        datetime_box.send_keys(time_)
        # ActionChains(self.browser).click(on_element=datetime_box).perform()

    @allure.step("Проверка правильности данных в таблице 'Transactions'")
    def check_table_content(self, table_content, deposit_sum):
        result = ""
        if len(table_content) != 2:
            result += "Amount of transaction must be 2.\n"
        for index, row in enumerate(table_content):
            if deposit_sum != int(row[2]):
                result += f"Deposite summa on row{index} is not equivalent to {deposit_sum}\n"
        return result

    @allure.step("Чтение данных из таблицы 'Transactions")
    def get_table_content(self):
        WebDriverWait(self.browser, TIME_WAIT_SHORT). \
            until(EC.presence_of_element_located(AccountPageLocators.TABLE_TRANSACTIONS))
        rows = len(self.browser.find_elements(*AccountPageLocators.TABLE_TRANSACTIONS_ROWS))
        cols = len(self.browser.find_elements(*AccountPageLocators.TABLE_TRANSACTIONS_FIRST_COL))

        table_content = []
        for row in range(1, rows + 1):
            one_row = []
            for col in range(1, cols + 1):
                value = self.browser.find_element(*AccountPageLocators.TABLE_CELL(row, col)).text
                one_row.append(value)
            table_content.append(one_row)

        return table_content
