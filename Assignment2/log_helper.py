import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import pytest




def pytest_configure():
    global driver
    global project_name

def login_helper():
    """
        Open URL and Login user with Emailaddress and Password
    """
    import pdb
    pdb.set_trace()
    chromedriver = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    service = Service(chromedriver)
    global driver
    driver = webdriver.Chrome(service=service, options=options) #instance of Webdriver
    driver.get("http://app.eks-cicd-18843.cicd.cnvrg.me")

    # Find the username and password input fields and login button
    emailaddress_field = pytest.driver.find_element(By.NAME, "email")
    password_field = pytest.driver.find_element(By.NAME, "password")
    login_button = pytest.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    # Enter the login credentials
    emailaddress_field.send_keys("test12233@mailinator.com")
    password_field.send_keys(123456)

    # Click the login button to login
    login_button.click()


def organization_helper():
    """
        Enter Organization Name
    """
    # Wait for the login process to complete
    WebDriverWait(pytest.driver, 10).until(EC.title_contains("Data Science Platform"))

    # Enter values into additional fields
    organization_field = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.NAME, "organization")))
    next_button = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))
    
    # Generate random organization name 
    org_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    organization_field.send_keys(org_name)

    next_button.click()


def skip():
    """
        Clicks on skip button
    """
    global driver
    WebDriverWait(driver, 10).until(EC.title_contains("Data Science Platform")) 
    skip_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Skip']")))
    skip_button.click()


def start_project():
    """
        Starts a new project
    """
    startproject_field = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-button.solid")))
    startproject_field.click()

    global project_name
    project_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    title_field = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, "title")))
    title_field.send_keys(pytest.project_name)

    continue_field = WebDriverWait(pytest.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='loading-button button button submit'] span")))
    continue_field.click()


def validate_project():
    """
        Validates the Project name 
    """
    test_project_name =WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".project-name"))).text

    global project_name
    if project_name == test_project_name:
        return True
    else:
        return False
    
