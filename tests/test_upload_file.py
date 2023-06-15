from pytest_bdd import given, when, then
from modules.upload_file.upload_file import *


@given('User signup a new user')
def step_def(browser):
    step_signup(browser)


@when('User enter the organization name')
def step_def(browser):
    step_organization(browser)


@when('User clicks on skip')
def step_def(browser):
    step_skip(browser)


@when('User starts a new project, enter the project title, select upload file and click continue')
def step_def(browser):
    step_startproject(browser)


@when('User select the file, click on upload and sync')
def step_def(browser):
    step_upload(browser)


@then('User verifies file name')
def step_def(browser):
    step_validate(browser)
