import pytest
from selene.support.shared import config, browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    #browser.quit()