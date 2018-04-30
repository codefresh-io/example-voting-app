import os
import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

ip = os.getenv('IP')

# Give Selenium Hub time to start
time.sleep(15)  # TODO: figure how to do this better


@pytest.fixture(scope='module')
def browser():
    browser = webdriver.Remote(
        command_executor='http://selenium_hub:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome'},
    )
    yield browser
    browser.quit()


def test_confirm_title(browser):
    browser.get("http://{}:80".format(ip))
    assert "Cats vs Dogs!" in browser.title


def test_confirm_choice_form(browser):
    browser.get("http://{}:80".format(ip))
    assert browser.find_element_by_id('choice') is True


def test_confirm_button_a(browser):
    browser.get("http://{}:80".format(ip))
    assert browser.find_element_by_id('a') is True


def test_confirm_button_b(browser):
    browser.get("http://{}:80".format(ip))
    assert browser.find_element_by_id('b') is True
