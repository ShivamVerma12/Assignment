from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random

project_name = None

def login(browser):
    """Open URL and Login user with Emailaddress and Password"""
    browser.get("http://app.gke-cicd-18883.cicd.cnvrg.me")

    # Find the username and password input fields and login button
    emailaddress_field = browser.find_element(By.NAME, "email")
    password_field = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    # Enter the login credentials
    emailaddress_field.send_keys("test25@mailinator.com")
    password_field.send_keys(123456)

    # Click the login button to login
    login_button.click()


def organization(browser):
    """Enter Organization Name"""
    # Wait for the login process to complete
    WebDriverWait(browser, 10).until(EC.title_contains("Data Science Platform"))

    # Enter values into additional fields
    organization_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "organization")))
    next_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

    # Generate random organization name
    org_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    organization_field.send_keys(org_name)

    next_button.click()

def skip(browser):
    """Calls skip to skip field """
    WebDriverWait(browser, 10).until(EC.title_contains("Data Science Platform"))
    skip_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Skip']")))
    skip_button.click()

def startproject(browser):
    """Class start_project to start a new project"""

    project_filed = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//nav[@class='organization-links'] //ul//a[1]")))
    project_filed.click()

    startproject_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-button.solid")))
    startproject_field.click()

    project_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    title_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "title")))
    title_field.send_keys(project_name)

    continue_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='loading-button button button submit'] span")))
    continue_field.click()

def validate(browser):
    """Validates the Project name"""
    test_project_name = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".project-name"))).text

    if project_name == test_project_name:
        return True
    else:
        return False
