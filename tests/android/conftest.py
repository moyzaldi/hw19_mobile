import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
import os
import sys
import os
import sys
import os

root_dir = os.path.abspath(os.path.dirname(__file__))

utils_dir = os.path.join(root_dir, 'utils')

sys.path.append(utils_dir)

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(params=[ "Samsung Galaxy S22"])
def mobile_management(request):
    deviceName = request.param
    options = UiAutomator2Options().load_capabilities({
        "deviceName": deviceName,

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": os.getenv("BSTACK_USER_NAME"),
            "accessKey": os.getenv("BSTACK_ACCESS_KEY")
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield
    attach.add_screenshot(browser)

    browser.quit()
