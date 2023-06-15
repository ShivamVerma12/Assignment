from pytest_bdd import given, when, then
from modules.register.signup import *


@given('User open desired url')
def step_def(browser):
    open_url(browser)


@when('User enter credentials and click Signup')
def step_def(browser):
    signup(browser)


@then('User verifies signin or not')
def step_def(browser):
    assert validate(browser)