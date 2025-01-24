import allure
import pytest
from selenium import webdriver
from api.BoardsApi import BoardApi
from conficuration.configprovider import ConfigProvider
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture
def browser():
    """Инициализирует веб-драйвер браузера и закрывает его после завершения теста."""
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().getint("ui", "browser_name")
        browser = None

        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Firefox()

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url , "2b754d81683a294766e6c752246cf680", "ATTA364916e089dbf35c7e30cb320b6deaf3b554bedfdac8def9620ec7d41eed5b50969511C6")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url , "", "")

@pytest.fixture
def dummy_board_id() -> str:
    url = ConfigProvider().get("api", "base_url")
    api = BoardApi(url , "2b754d81683a294766e6c752246cf680", "ATTA364916e089dbf35c7e30cb320b6deaf3b554bedfdac8def9620ec7d41eed5b50969511C6")
    res = api.create_board("Board to be deleted").get("id")
    return res

@pytest.fixture
def delete_board() -> any:
    dictionary = {"board_id": ""}
    yield dictionary
    url = ConfigProvider().get("api", "base_url")
    api = BoardApi(url , "2b754d81683a294766e6c752246cf680", "ATTA364916e089dbf35c7e30cb320b6deaf3b554bedfdac8def9620ec7d41eed5b50969511C6")
    api.delete_board_by_id(dictionary.get("board_id"))