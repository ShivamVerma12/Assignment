from pytest_bdd import given, when, then
from modules.filter.filter import *

@given('user open url')
def step_def(browser):
    open_url(browser)

@when('user search the product, apply filter and click on first result')
def step_def(browser):
    apply_filter(browser)

@then('user validate with filter')
def step_def(browser):
    assert validate(browser)