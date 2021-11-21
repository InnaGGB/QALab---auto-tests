import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb", "en", "af", "az", "fr","zh-HK","it"])
def test_localization(browser, language):
    link = f"https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2F&hl={language}&dsh=S1024190498%3A1637501724396787&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
    browser.get(link)
    time.sleep(3)