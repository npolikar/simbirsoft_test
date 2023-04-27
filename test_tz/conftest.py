# import pytest
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Remote(command_executor="http://192.168.56.1:4444/wd/hub",
                              desired_capabilities={'browserName': "chrome", 'javascriptEnabled': True})
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="function")
def browser_single():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()
