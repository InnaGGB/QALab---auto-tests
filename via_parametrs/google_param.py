import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def test_language_switcher_exists(browser):
    link = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2F&hl={language}&dsh=S1024190498%3A1637501724396787&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
    browser.get(link)
    time.sleep(3)
    switcher = browser.find_elements_by_xpath('//*[@id="lang-chooser"]/div[1]/div[1]/div[4]')
    assert switcher, "No 'Language switcher' listbox"