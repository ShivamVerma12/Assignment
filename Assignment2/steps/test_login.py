from behave import given, when, then
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

chromedriver = os.environ.get("chromedriver")


@given('User login with credentials')
def login(context):
    """Open URL and Login user with Emailaddress and Password"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    context.driver = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    context.driver.get("http://app.gke-cicd-18883.cicd.cnvrg.me")

    # Find the username and password input fields and login button
    emailaddress_field = context.driver.find_element(By.NAME, "email")
    password_field = context.driver.find_element(By.NAME, "password")
    login_button = context.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    # Enter the login credentials
    emailaddress_field.send_keys("test123456789@mailinator.com")
    password_field.send_keys(123456)

    # Click the login button to login
    login_button.click()


@when('User enter the organization name')
def organization(context):
    """Enter Organization Name"""
    # Wait for the login process to complete
    WebDriverWait(context.driver, 10).until(EC.title_contains("Data Science Platform"))

    # Enter values into additional fields
    organization_field = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.NAME, "organization")))
    next_button = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

    # Generate random organization name
    org_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    organization_field.send_keys(org_name)

    next_button.click()


@when('User clicks on skip')
def step_def(context):
    """Calls skip to skip field """
    WebDriverWait(context.driver, 10).until(EC.title_contains("Data Science Platform"))
    skip_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Skip']")))
    skip_button.click()


@when('User starts a new project, enter the project title and click continue')
def step_def(context):
    """Class start_project to start a new project"""
    startproject_field = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".new-project")))
    startproject_field.click()
    # startproject_field = WebDriverWait(context.driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-button.solid")))
    # startproject_field.click()

    context.project_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    title_field = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, "title")))
    title_field.send_keys(context.project_name)

    continue_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='loading-button button button submit'] span")))
    continue_field.click()


@then('User verifies project name')
def step_def(context):
    """Validates the Project name"""
    test_project_name = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".project-name"))).text

    assert context.project_name == test_project_name
