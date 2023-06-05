from pytest_bdd import scenario, given, when, then
from urllib.parse import urlparse, parse_qs
from helper import helper, simulate_typing, validate


@scenario('chrome_script.feature', 'Open Google Chrome and on search bar type w3school and press enter')
def test_chrome_script():
    print("Chrome open with w3schools on search bar")
    pass


@given('Open Google Chrome browser')
def open_chrome():
    """Calling Helper Function"""
    helper()


@when('On search bar type w3school and press enter key')
def write_url():
    """Calling Simulate_Typing Function"""
    simulate_typing()


@then('Checking the url open in chrome is desired or not')
def validate_url():
    """Calling Validate Function"""
    search_text = validate()
    assert search_text == "https://w3schools.com/"
