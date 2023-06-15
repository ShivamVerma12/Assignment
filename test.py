from web_driver.driver import browser
from pytest_bdd import scenarios
from tests.test_chrome import *
from tests.test_login import *
from tests.test_signup import *
from tests.test_search_product import *
from tests.test_filter import *
from tests.test_upload_file import *

scenarios('feature_file/chrome.feature')
