from selenium.webdriver.common.by import By
from behave import *


@when('user search the product, apply filter and click on first result')
def apply_filter(context):
    search_field = context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_field.send_keys("smartphone 128gb")

    search = context.driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
    search.click()

    # Apply filter
    storage_filter_link = context.driver.find_element(By.LINK_TEXT, "128 GB")
    storage_filter_link.click()

    # Find the first product link
    first_product = context.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")
    first_product_link = first_product.get_attribute("href")

    # Extract the product name from the first product element
    context.product_name = first_product.find_element(By.CSS_SELECTOR, "h2 a span").text

    # Open the first product in a new tab
    context.driver.execute_script("window.open(arguments[0]);", first_product_link)


@then('user validate with filter')
def validate(context):
    """Validate data"""
    assert "128gb" in context.product_name.lower() or "128 gb" in context.product_name.lower()
    context.driver.quit()
