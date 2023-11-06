import pytest
from selenium import  webdriver

@pytest.fixture(scope="function")
def browser():
    print("\n===  Start browser for test  ===")
    browser = webdriver.Chrome()
    yield browser
    print("\n===  Shutdown browser    ===")
    browser.quit()