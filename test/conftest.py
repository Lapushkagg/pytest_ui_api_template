import allure
import pytest
from selenium import webdriver
from api.BoardsApi import BoardApi
from conficuration.configprovider import ConfigProvider
from testdata.DataProvider import DataProvider


@pytest.fixture
def browser():
    """Инициализирует веб-драйвер браузера и закрывает его после завершения теста."""
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")
        browser = None

        if browser_name == "chrome":
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
    test_data = {
        "api_key": DataProvider().get_api_key(),
        "token": DataProvider().get_token(),
        "org_id": DataProvider().get("org_id"),
    }
    return BoardApi(url, test_data)


@pytest.fixture
def test_data():
    """Фикстура для предоставления тестовых данных."""
    return {
        "api_key": DataProvider().get_api_key(),
        "token": DataProvider().get_token(),
        "org_id": DataProvider().get("org_id"),
        "email": DataProvider().get("email"),
        "password": DataProvider().get("password"),
        "username": DataProvider().get("username"),
    }


@pytest.fixture
def dummy_board_id(api_client: BoardApi) -> str:
    """Создаёт временную доску для теста."""
    res = api_client.create_board("Board to be deleted")
    return res.get("id")


@pytest.fixture
def delete_board(api_client: BoardApi) -> dict:
    """Удаляет доску после завершения теста."""
    dictionary = {"board_id": ""}
    yield dictionary
    if dictionary.get("board_id"):
        api_client.delete_board_by_id(dictionary.get("board_id"))
