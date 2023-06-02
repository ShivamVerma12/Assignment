import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse, parse_qs
import pyautogui as df
from pynput.keyboard import Key, Controller
import pytest


def pytest_configure():
    pytest.driver


def helper():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    chromedriver = "/usr/local/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    service = Service(chromedriver)
    pytest.driver = webdriver.Chrome(service=service, options=options)
    pytest.driver.get("http://google.com")


def simulate_typing():
    keyboard = Controller()
    df.typewrite("https://w3schools.com/")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def validate():
    my_current_url = pytest.driver.current_url
    print("Current URL:", my_current_url)
    # Parse the URL
    parsed_url = urlparse(my_current_url)

    # Extract the query parameters
    query_params = parse_qs(parsed_url.query)

    # Fetch the search bar text
    search_text = query_params.get('q', [''])[0]
    # Perform the desired validation
    return search_text
