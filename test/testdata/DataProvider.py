import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'test_data.json')
with open(file_path, encoding='utf-8') as my_file:
    global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop:str) -> str:
        return self.data.get(prop)

    def getint(self, prop:str) -> int:
        val = self.data.get(prop)
        return int(val)

    def get_token(self) -> str:
        return self.data.get("token")
    
    def get_api_key(self) -> str:
        return self.data.get("api_key")