from pytest_bdd import given, when, then

from modules.chrome.chrome import *


@given('Open Google Chrome browser')
def open_chrome(browser):
    """Calling Helper Function"""
    setup(browser)


@when('On search bar type w3school and press enter key')
def write_url():
    """Calling Simulate_Typing Function"""
    simulate_typing()


@then('Checking the url open in chrome is desired or not')
def validate_url(browser):
    """Calling Validate Function"""
    assert validate(browser)
