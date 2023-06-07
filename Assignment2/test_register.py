from pytest_bdd import scenario, given, when, then
from register_helper import helper,signup,validate

@scenario('register.feature','User register new User')
def success():
    print("Success")
    pass

@given('User open desired url')
def open_url():
    helper()

@when('User enter credentials and click Signup')
def register_user():
    signup()

@then('User verifies signin or not')
def validate_user():
    assert validate()