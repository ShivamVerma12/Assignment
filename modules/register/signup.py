from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


def open_url(browser):
    """Open URL """
    browser.get("http://app.gke-cicd-18883.cicd.cnvrg.me")


def signup(browser):
    """Sign up new user"""
    signup_field = browser.find_element(By.CSS_SELECTOR, "a[href='/users/sign_up']")
    signup_field.click()

    emailaddress_field = browser.find_element(By.NAME, "email")
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    signup_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    email = str(''.join(random.choices(string.ascii_letters, k=6)))
    password = random.random()
    emailaddress_field.send_keys(email + "@mailinator.com")
    username_field.send_keys(email)
    password_field.send_keys(password)
    signup_button.click()


def validate(browser):
    """Validate data"""
    organization_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "organization")))

    if organization_field is not None:
        return True

    else:
        return False
