import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse, parse_qs
import pyautogui as df
from pynput.keyboard import Key, Controller


chromedriver = os.environ.get("chromedriver")
url = os.environ.get("url")

driver = None
def pytest_configure():
    global driver # Global variable 


def helper():
    """
        Helper Function for opening Google Chrome
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) 
    service = Service(chromedriver)
    global driver
    driver = webdriver.Chrome(service=service, options=options) #instance of Webdriver
    driver.get("http://google.com")


def simulate_typing():
    """
        Function for typing desired text on search bar
    """
    keyboard = Controller() # Controller instance
    df.typewrite(url) # typibg text on search bar
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def validate():
    """ 
        Validation Function
    """
    my_current_url = driver.current_url # Fetch the current url

    parsed_url = urlparse(my_current_url)    # Parse the URL
    query_params = parse_qs(parsed_url.query)     # Extract the query parameters
    search_text = query_params.get('q', [''])[0]     # Fetch the search bar text

    return search_text
