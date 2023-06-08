import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from behave import *

chromedriver = os.environ.get("chromedriver")
productName = os.environ.get("product_name")


@given('user open url')
def open_url(context):
    """Opens desired url"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(chromedriver)
    context.driver = webdriver.Chrome(service=service, options=options)  # instance of Webdriver
    context.driver.get("http://amazon.com")


@when('user search the product and click on first result')
def search(context):
    """Searches for the product"""
    search_field = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_field.send_keys(productName)

    search = context.driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
    search.click()

    # Find the first product link
    first_product = context.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")
    first_product_link = first_product.get_attribute("href")

    # Extract the product name from the first product element
    context.product_name = first_product.find_element(By.CSS_SELECTOR, "h2 a span").text

    # Open the first product in a new tab
    context.driver.execute_script("window.open(arguments[0]);", first_product_link)


@then('user validate with product name')
def validate(context):
    """Validate data"""
    assert productName.lower() in context.product_name.lower()
    context.driver.quit()
