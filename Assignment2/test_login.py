from pytest_bdd import scenario, given, when, then
from log_helper import login_helper, organization_helper, skip,start_project, validate_project
from pathlib import Path


scenario("test_login.feature", "user creating a new project")

@given('user login with credentials')
def login():
    """Calls login_helper to login user with credentials"""
    print("in given")
    import pdb 
    pdb.set_trace()
    login_helper()


@when('user enter the organization name')
def organization():
    """Calls organization_helper to enter organization name"""
    organization_helper()


@when('user clicks on skip')
def step_def():
    """Calls skip to skip field """
    skip()

    
@when('user starts a new project, enter the project title and click continue')
def step_def():
    """Class start_project to start a new project"""
    start_project()


@then('user verifies project name')
def step_def():
    """ Calls Validate function"""
    assert validate_project()
