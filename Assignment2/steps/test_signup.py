import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
from behave import given, when, then

chromedriver = os.environ.get("chromedriver")


@given('User open desired url')
def open_url(context):
    """Open URL """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    context.driver = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    context.driver.get("http://app.gke-cicd-18883.cicd.cnvrg.me")


@when('User enter credentials and click Signup')
def signup(context):
    """Sign up new user"""
    signup_field = context.driver.find_element(By.CSS_SELECTOR, "a[href='/users/sign_up']")
    signup_field.click()

    emailaddress_field = context.driver.find_element(By.NAME, "email")
    username_field = context.driver.find_element(By.NAME, "username")
    password_field = context.driver.find_element(By.NAME, "password")
    signup_button = context.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    email = str(''.join(random.choices(string.ascii_letters, k=6)))
    password = random.random()
    emailaddress_field.send_keys(email + "@mailinator.com")
    username_field.send_keys(email)
    password_field.send_keys(password)
    signup_button.click()


@then('User verifies signin or not')
def validate(context):
    """Validate data"""
    organization_field = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.NAME, "organization")))

    assert organization_field
