from pytest_bdd import given, when, then
from modules.search.seacrh_product import *


@given('user open url')
def step_def(browser):
    open_url(browser)


@when('user search the product and click on first result')
def step_def(browser):
    search(browser)


@then('user validate with product name')
def step_def(context):
    assert validate(context)