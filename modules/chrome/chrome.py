from urllib.parse import urlparse, parse_qs

from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import pyautogui as df
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from web_driver.driver import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def setup(browser):
    """
        Helper Function for opening Google Chrome
    """
    browser.get("http://google.com")


def simulate_typing():
    """
        Function for typing desired text on search bar
    """
    # search = browser.find_element(By.XPATH, "//input[id='input']")
    # search.send_keys("https://w3schools.com/")
    keyboard = Controller()  # Controller instance
    df.typewrite("https://w3schools.com/")  # typing text on search bar
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def validate(browser):
    """
        Validation Function
    """
    # browser = webdriver.Chrome()
    my_current_url = browser.current_url
    parsed_url = urlparse(my_current_url)
    query_params = parse_qs(parsed_url.query)
    search_text = query_params.get('q', [''])[0]
    if search_text in "https://w3schools.com/":
        return True
    else:
        return False
