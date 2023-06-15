from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.set_page_load_timeout(3000)
    yield driver
    driver.quit()
