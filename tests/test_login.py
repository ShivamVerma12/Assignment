from pytest_bdd import scenario, when, then, given
from modules.login.login import *


@given('User login with credentials')
def step_login(browser):
    login(browser)


@when('User enter the organization name')
def step_def(browser):
    organization(browser)


@when('User clicks on skip')
def step_def(browser):
    skip(browser)


@when('User starts a new project, enter the project title and click continue')
def step_def(browser):
    startproject(browser)


@then('User verifies project name')
def step_def(browser):
    assert validate(browser)
