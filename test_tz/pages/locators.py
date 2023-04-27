from selenium.webdriver.common.by import By


class LoginPageLocators:

    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[text()='Customer Login']")
    YOUR_NAME_FIELD = (By.TAG_NAME, "select")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")


class AccountPageLocators:

    TRANSACTIONS_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-lg tab')][1]")

    DEPOSIT_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-lg tab')][2]")
    AMOUNT_TO_BE_DEPOSITED_INPUT = (By.CSS_SELECTOR, "input, [type='number']")
    DEPOSIT_BUTTON_CONFIRM = (By.XPATH, "//button[text()='Deposit']")
    DEPOSIT_SUCCESSSFUL_SPAN = (By.XPATH, "//span[text()='Deposit Successful']")

    WITHDRAWL_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-lg tab')][3]")
    AMOUNT_TO_BE_WITHDRAWL_INPUT = (By.XPATH, "//div[@class='form-group']/input")
    AMOUNT_TO_BE_WITHDRAWL_LABEL = (By.XPATH, "//label[text()='Amount to be Withdrawn :']")
    WITHDRAWL_BUTTON_CONFIRM = (By.XPATH, "//button[text()='Withdraw']")
    WITHDRAWL_SUCCESSSFUL_SPAN = (By.XPATH, "//span[text()='Transaction successful']")

    BALANCE_LABEL = (By.XPATH, "//div[@class='center']/strong[2]")

    BACK_BUTTON = (By.XPATH, "//button[text()='Back']")
    START_BUTTON = (By.CSS_SELECTOR, "#start")

    TABLE_TRANSACTIONS = (By.XPATH, "//table")
    TABLE_TRANSACTIONS_ROWS = (By.XPATH, "//tbody/tr")
    TABLE_TRANSACTIONS_FIRST_COL = (By.XPATH, "//tbody/tr[1]/td")

    @classmethod
    def TABLE_CELL(cls,tr_number: int, td_number: int):
        return (By.XPATH, f"//tbody/tr[{tr_number}]/td[{td_number}]")
