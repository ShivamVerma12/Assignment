from selenium.webdriver.common.by import By


def open_url(browser):
    """Opens desired url"""
    browser.get("http://amazon.com")


def apply_filter(browser, context):
    search_field = browser.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    search_field.send_keys("smartphone 128gb")

    search = browser.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
    search.click()

    # Apply filter
    storage_filter_link = browser.find_element(By.LINK_TEXT, "128 GB")
    storage_filter_link.click()

    # Find the first product link
    first_product = browser.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result'] h2 a")
    first_product_link = first_product.get_attribute("href")

    # Extract the product name from the first product element
    context.product_name = first_product.find_element(By.CSS_SELECTOR, "h2 a span").text

    # Open the first product in a new tab
    browser.execute_script("window.open(arguments[0]);", first_product_link)


def validate(browser, context):
    """Validate data"""
    if "128gb" in context.product_name.lower() or "128 gb" in context.product_name.lower():
        return True
    else:
        return False
