import os
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    InvalidSelectorException,
    NoSuchElementException,
    WebDriverException)

vote_endpoint_ip = os.getenv('VOTE_ENDPOINT_IP')

# Give Selenium Hub time to start
time.sleep(15)  # TODO: figure how to do this better

@pytest.fixture(scope='module')
def browser():
    browser_name = ip = os.getenv('BROWSER')
    browser = webdriver.Remote(
        command_executor='http://selenium_hub:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome'},
    )
    yield browser
    browser.quit()


def test_confirm_title(browser):
    browser.get("http://{}:80".format(vote_endpoint_ip))
    assert "Cats vs Dogs!" in browser.title


def test_confirm_choice_form(browser):
    browser.get("http://{}:80".format(vote_endpoint_ip))
    element = browser.find_element(By.ID, 'choice')
    assert element.get_attribute('id') == 'choice'


def test_confirm_button_a(browser):
    browser.get("http://{}:80".format(vote_endpoint_ip))
    element = browser.find_element(By.ID, 'a')
    assert element.get_attribute('id') == 'a'


def test_confirm_button_b(browser):
    browser.get("http://{}:80".format(vote_endpoint_ip))
    element = browser.find_element(By.ID, 'b')
    assert element.get_attribute('id') == 'b'
