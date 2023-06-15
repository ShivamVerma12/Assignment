import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random
import pyautogui



def step_signup(browser):
    """Sign up a new user"""
    chromedriver = "/usr/local/bin/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    browser = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    browser.maximize_window()
    browser.get("http://app.eks-cicd-18945.cicd.cnvrg.me")
    signup_field = browser.find_element(By.CSS_SELECTOR, "a[href='/users/sign_up']")
    signup_field.click()

    email_field = browser.find_element(By.NAME, "email")
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    signup_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

    email = str(''.join(random.choices(string.ascii_letters, k=6)))
    password = random.random()
    email_field.send_keys(email + "@mailinator.com")
    username_field.send_keys(email)
    password_field.send_keys(password)
    signup_button.click()



def step_organization(browser):
    """Create new organization"""
    # Enter values into additional fields
    organization_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "organization")))
    next_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

    # Generate random organization name
    org_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    organization_field.send_keys(org_name)

    next_button.click()



def step_skip(browser):
    """Skips field"""
    skip_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Skip']")))
    skip_button.click()



def step_startproject(browser):
    """Create new project"""
    project_filed = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//nav[@class='organization-links'] //ul//a[1]")))
    project_filed.click()

    startproject_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".rounded-button.solid")))
    startproject_field.click()

    project_name = str(''.join(random.choices(string.ascii_letters, k=6)))
    title_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "title")))
    title_field.send_keys(project_name)

    upload_field = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Upload Files']")))

    upload_field.click()

    continue_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='loading-button button button submit'] span")))
    continue_field.click()



def step_upload(browser):
    drag_field = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "my-dropzone")))
    drag_field.click()

    # Open the file manager
    pyautogui.hotkey('super')
    time.sleep(2)

    # Activate the search functionality
    pyautogui.press('')
    pyautogui.typewrite("experiment.rb")

    time.sleep(2)
    # Press Enter to perform the search
    pyautogui.press('down')
    pyautogui.press('enter', presses=2)

    upload = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='submit-all-files']")))
    upload.click()
    sync = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Sync ']")))
    sync.click()



def step_validate(browser):
    verify = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='experiment.rb']"))).text

    if verify is not None:
        return True
    else:
        return False

