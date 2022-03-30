import unittest
import requests
from unittest.mock import patch


class Food:
    def __init__(self, name):
        self.name = name

    def get_nutrients(self):
        return requests.get("/our/food/rapidapi/url/" + self.name)


def get_returns_nutrients_for_eggs(i):
    print(i)
    return {"protein": 6, "fats": 6}


class MyTestCase(unittest.TestCase):
    @patch("requests.get", get_returns_nutrients_for_eggs)
    def test_we_get_nutrition_info_for_eggs(self):
        # set up
        egg = Food("egg")
        # execution
        nutrients = egg.get_nutrients()
        # assertion
        self.assertEqual({"protein": 6, "fats": 6}, nutrients)


if __name__ == '__main__':
    unittest.main()
