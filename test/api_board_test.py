from api.BoardsApi import BoardApi

url = "https://api.trello.com/1"
api_key = "2b754d81683a294766e6c752246cf680"  # Ваш API ключ
token = "ATTA364916e089dbf35c7e30cb320b6deaf3b554bedfdac8def9620ec7d41eed5b50969511C6"

def test_get_boards(api_client: BoardApi):
    board_list = api_client.get_all_boards_by_org_id("6791fd008ad71f14a253764e")
    print(board_list)


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("6791fd008ad71f14a253764e")

    res = api_client.create_board("Test board")
    delete_board["board_id"] = res.get("id")
    board_list_after = api_client.get_all_boards_by_org_id("6791fd008ad71f14a253764e")

    assert len(board_list_after) - len(board_list_before) == 1

def test_delete_board(api_client: BoardApi,dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id("6791fd008ad71f14a253764e")

    api_client.delete_board_by_id(dummy_board_id)

    board_list_after = api_client.get_all_boards_by_org_id("6791fd008ad71f14a253764e")

    assert len(board_list_before) - len(board_list_after) == 1