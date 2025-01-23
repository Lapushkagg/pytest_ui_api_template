import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """Инициализирует веб-драйвер браузера и закрывает его после завершения теста."""
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()