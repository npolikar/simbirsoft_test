from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from .base_page import BasePage
from .locators import LoginPageLocators


TIME_WAIT_LONG = 5
TIME_WAIT_SHORT = 3


class LoginPage(BasePage):
    @allure.step("Нажатие на кнопку 'Customer Login'")
    def click_on_customer_login_button(self):
        login_link = self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN_BUTTON)
        login_link.click()

    @allure.step("Выбор имени пользователя")
    def select_your_name(self, name: str = "Harry Potter"):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.YOUR_NAME_FIELD))
        select_your_name = Select(self.browser.find_element(*LoginPageLocators.YOUR_NAME_FIELD))
        select_your_name.select_by_visible_text(name)

    @allure.step("Нажатие на кнопку 'Login' после выбора пользователя")
    def click_on_login_button(self):
        login_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        login_button.click()

