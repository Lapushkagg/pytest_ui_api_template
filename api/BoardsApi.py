import requests


class BoardApi:
    def __init__(self, base_url: str, test_data: dict) -> None:
        self.base_url = base_url
        self.api_key = test_data.get("api_ke")
        self.token = test_data.get("token")

    def get_all_boards_by_org_id(self, test_data: dict) -> dict:
        """Получить список всех досок по ID организации."""
        url = f"{self.base_url}/organizations/{test_data.get("org_id")}"
        params = {
            "key": self.api_key,
            "token": self.token,
            "boards": "open",  # Включаем только открытые доски
            "board_fields": "all",  # Поля досок
            "fields": "boards"  # Поля организации
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Вызывает ошибку, если запрос не успешен
        return response.json().get("boards")

    def create_board(self, name: str, default_lists: bool = True) -> dict:
        """Создать новую доску."""
        path = f"{self.base_url}/boards/"
        params = {
            "key": self.api_key,  # Добавление API-ключа
            "token": self.token    # Добавление токена
        }
        body = {
            "name": name,
            "defaultLists": default_lists,
        }
        # Используем params для ключа и токена, и передаем тело запроса как json
        resp = requests.post(path, params=params, json=body)
        resp.raise_for_status()  # Проверка на ошибки
        return resp.json()

    def delete_board_by_id(self, board_id: str) -> dict:
        """Удалить доску по ID."""
        path = f"{self.base_url}/boards/{board_id}"
        params = {
            "key": self.api_key,  # Добавление API-ключа
            "token": self.token    # Добавление токена
        }
        resp = requests.delete(path, params=params)
        resp.raise_for_status()  # Проверка на ошибки
        return resp.json()