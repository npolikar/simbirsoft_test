import pytest

from .pages.login_page import LoginPage
from .pages.account_page import AccountPage
from .services.calc_service import get_fibonachi_of_current_day, check_table_content, save_transaction_to_csv_file

import time
import allure

"""
pytest --alluredir="c:/Private/simbirsk/"
allure serve "c:/Private/simbirsk/"   
"""


@allure.feature("Some sheet")
@pytest.mark.parametrize("user_name, transactions_file", [("Harry Potter", "transactions.csv"),])
def test_xyz_bank(browser, user_name, transactions_file):
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page_login = LoginPage(browser, link)
    page_login.open()
    page_login.click_on_customer_login_button()
    page_login.select_your_name(user_name)
    page_login.click_on_login_button()

    deposit_sum = get_fibonachi_of_current_day()
    page_account = AccountPage(browser, link)

    # Deposit
    page_account.click_on_deposit_button()
    page_account.set_deposit_amount(deposit_sum)
    page_account.click_on_deposit_button_confirm()
    assert page_account.check_deposit_successful_message(), "After Deposit execute red text 'Deposit Successful' must be on form"

    # Withdrawl
    page_account.click_on_withdrawl_button()
    page_account.set_withdrawl_amount(deposit_sum)
    page_account.click_on_withdrawl_button_confirm()
    assert page_account.check_withdrawl_successful_message(), "After Withdrawl execute red text 'Transaction successful' must be on form"

    # Balance
    balance = page_account.get_balance()
    assert balance == 0, "Balance after Withdrawl must be zero."

    # Transactions
    page_account.click_on_transactions_button()
    page_account.set_start_datetime_v2()
    table_content = page_account.get_table_content()

    while not table_content:
        page_account.click_on_back()
        time.sleep(1)
        page_account.click_on_transactions_button()
        page_account.set_start_datetime_v2()
        table_content = page_account.get_table_content()

    table_check_errors = check_table_content(table_content, deposit_sum)
    assert len(table_check_errors) == 0, table_check_errors

    save_transaction_to_csv_file(table_content, transactions_file)
