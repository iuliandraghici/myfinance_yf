import json


class Configuration:
    def __init__(self):
        file = open("config.json")
        contents = file.read()
        file.close()
        self.conf = json.loads(contents)

    def get_number_of_items_per_page(self) -> int:
        return self.conf["number_of_items_per_page"]
