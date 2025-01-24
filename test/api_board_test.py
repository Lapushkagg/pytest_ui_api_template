import allure
from api.BoardsApi import BoardApi


def test_get_boards(api_client: BoardApi, test_data: dict):
    board_list = api_client.get_all_boards_by_org_id(test_data.get("org_id"))
    print(board_list)


def test_create_board(api_client: BoardApi, delete_board: dict, test_data: dict):
    board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    res = api_client.create_board("Test board")
    delete_board["board_id"] = res.get("id")

    board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    assert len(board_list_after) - len(board_list_before) == 1


def test_delete_board(api_client: BoardApi, dummy_board_id: str, test_data: dict):
    board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"))

    assert len(board_list_before) - len(board_list_after) == 1