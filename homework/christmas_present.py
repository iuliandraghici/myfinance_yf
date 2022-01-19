# dict1 = {"a": 1, "b": 3, "c": 6, "d": 10, "e": 90, "f": 15}
#
#
# # ex1 - define a function which returns the keys of a dictionary as a list
# #     dict1.keys()
# # ex2 - define a function which returns the biggest number from a dictionary
# #     max(dict1.values())
# def max_of_dict(d: dict):
#     return max(d.values())
#
#
# max = max_of_dict(dict1)
# print(max)
#
#
# # ex3 - define a function which removes all odd numbers from a dictionary
# def remove_odd_numbers(d: dict):  # we create a new list w/o the odd numbers
#     return {k: v for k, v in d.items() if v % 2 == 0}
#
#
# dict1 = remove_odd_numbers(dict1)
# print(dict1)
# #   dict1.pop(k)  remove the key, but not in for
#
#
# tuple1 = ("a", "b", "c", "d")
# tuple2 = (1, 2, 3, 4)
#
#
# # ex4 - define a function which receives 2 tuples and creates a dictionary (one tuple will become the keys)
# def create_dict_from_tuples(tuple1: tuple, tuple2: tuple) -> dict:
#     new_dict = {}
#     i = 0
#     while i < len(tuple1) or i < len(tuple2):
#         key = tuple1[i]
#         value = tuple2[i]
#         new_dict[key] = value
#         i = i + 1
#     return new_dict
#
#
# dict4 = create_dict_from_tuples(tuple1, tuple2)
#
#
# # ex5 - define a function which makes the sum of the values from a dictionary
# #     sum(dict1.values())
# # ex6 - define a function which creates a string from the keys of a dictionary
def create_string_from_keys(dict1: dict) -> str:
    keys = dict1.keys() # collect the keys
    return "-".join(keys)  # glue/join them in a string
#
#
# str2 = create_string_from_keys(dict4)
# print(str2)
#
# prices = {"iphone": 1000, "samsung": 800, "pixel": 600, "allview": 100, "nokia": 200, "oppo": 600}
#
#
# # ex7 - define a function which receives a dictionary (keys are the phone, values are the price)
# # and the budget (min & max) and return all the phones which are in the price interval
# def get_phones(phones: dict, min: int, max: int):
#     lista = []
#     for key, value in phones.items():
#         if min <= value <= max:
#             lista.append(key)
#     return lista
#
#
# print(get_phones(prices, 500, 900))
#
# accounts = [
#     {"user": "Bob", "account": 0, "debt": 500},
#     {"user": "Alice", "account": 2000, "debt": 0},
#     {"user": "Leo", "account": 600, "debt": 2000},
#     {"user": "Ralph", "account": 5000, "debt": 1000},
#     {"user": "Matilda", "account": 100, "debt": 0}
# ]
# # ex8 - define a function which receives a list like the one above and returns the user with the biggest account and
# # the user with the biggest difference between debt and account
# max_account = None
# for user in accounts:
#     if not max_account:  # if max_account is None, we initialize it
#         max_account = user
#     if max_account and max_account["account"] < user["account"]:
#         max_account = user
# print(max_account["user"])
#
# max_diff = None
# for user in accounts:
#     if not max_diff:
#         max_diff = user
#     elif max_diff["debt"] - max_diff["account"] < user["debt"] - user["account"]:
#         max_diff = user
# print(max_diff["user"])
#
# # ex9 - ask the user to give a name, email and telephone and write to a dict, print the dict
# user = input("What is your name?")
# email = input("What is your email?")
# tel = input("What is your phone number?")
# d = {"user": user, "email": email, "tel": tel}
# print(d)


# ex10 - create a rock, paper, scissors game with the user's input
# pick a random choice of the computer
# a take the user's input
# compare the choices and select the winner

def rock_paper_scissors():
    import random
    computer = random.choice(["rock", "paper", "scissors"])
    user = input("Pick rock, paper or scissors: ")
    if not user in ["rock", "paper", "scissors"]:
        print("Ce faci aici?")
        return
    if computer == user:
        print("Egalitate!")
    elif (user, computer) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        print("You won! Computer picked " + computer)
    else:
        print("The computer won! You lost, loser! It picked " + computer)

turns = input("How many turns you want to play? ")
for i in range(int(turns)):
    rock_paper_scissors()
