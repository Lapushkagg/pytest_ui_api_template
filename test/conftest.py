import allure
import pytest
from selenium import webdriver
from api.BoardsApi import BoardApi
from conficuration.configprovider import ConfigProvider
from selenium.webdriver.firefox.service import Service as FirefoxService
from testdata.DataProvider import DataProvider


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
    test_data = DataProvider().data  # Получаем словарь данных
    return BoardApi(url, test_data)  # Передаем весь словарь как test_data

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url , "", "")

@pytest.fixture
def dummy_board_id() -> str:
    url = ConfigProvider().get("api", "base_url")
    api = BoardApi(url , DataProvider().get_api_key(),  DataProvider().get_token())
    res = api.create_board("Board to be deleted").get("id")
    return res

@pytest.fixture
def delete_board() -> any:
    dictionary = {"board_id": ""}
    yield dictionary
    url = ConfigProvider().get("api", "base_url")
    api = BoardApi(url , DataProvider().get_api_key(),  DataProvider().get_token())
    api.delete_board_by_id(dictionary.get("board_id"))

@pytest.fixture
def test_data():
    return DataProvider()