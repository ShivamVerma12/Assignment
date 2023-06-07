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
    pytest.driver

def helper():
    chromedriver = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    service = Service(chromedriver)
    # global driver
    pytest.driver = webdriver.Chrome(service=service, options=options) #instance of Webdriver
    pytest.driver.get("http://app.eks-cicd-18843.cicd.cnvrg.me")


def signup():
    global driver
    signup_field = pytest.driver.find_element(By.CSS_SELECTOR, "a[href='/users/sign_up']")
    signup_field.click()

    emailaddress_field = pytest.driver.find_element(By.NAME, "email")
    username_field = pytest.driver.find_element(By.NAME, "username")
    password_field = pytest.driver.find_element(By.NAME, "password")
    signup_button = pytest.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    email = str(''.join(random.choices(string.ascii_letters, k=6)))
    password = random.random()
    emailaddress_field.send_keys(email +"@mailinator.com")
    username_field.send_keys(email)
    password_field.send_keys(password)
    print(password)
    signup_button.click()

def validate():
    # global driver
    organization_field = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.NAME, "organization")))
    if organization_field:
        return True
    
    else:
        return False
    
# helper()
