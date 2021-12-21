# This exercises are for the input function
# you can play a little with the function here https://www.w3schools.com/python/ref_func_input.asp

# ex1
# take 2 numbers from the user
# print the sum back

def input_sum():
    num1 = input("Enter first number: ")  # ask for the first number, num1 equals user's input
    num2 = input("Enter second number: ")
    sum = float(num1) + float(num2)  # we have to convert the user's input from string to float
    print("The sum is " + str(sum))

# ex2
# take 3 numbers from the user
# print the biggest one
# numbers = input("Type the numbers separated by space: ")
# lista = numbers.split(" ")  # split function returns a list of substrings
# lista_int = [float(x) for x in lista]  # this will do append for the code before `for`
# # lista_int = [] # create an empty list to put the number values
# # for x in lista:
# #     lista_int.append(float(x)) # add every string from lista after we transform it
#
# print(lista_int)
# biggest_number = max(lista_int)  # provide the list of the numbers to max function, will return the biggest number
# print("Biggest number = " + str(biggest_number))

# ex3
# ask the user's name
# ask him his age
# print if he is allowed to drink
# name = input("What is your name? ")
# age = int(input("What is your age?"))
# if age >= 18:
#     print(name + " is allowed")
# else:
#     print(name + " is not allowed")

# ex4
# ask the user for 5 words
# put them in a sentence
# sentence = ""
# for x in range(5):  # range(5) -> [0, 1, 2, 3, 4]
#     sentence = sentence + " " + input("Type a word")
# print(sentence)

# ex5
import random

x = random.randint(0, 9)  # this will pick a random number between 0 and 9
# create a guessing game, the user must tell a number between 0 and 9 and you must tell him if he guessed it
tries = 0
max_tries = 3
user_nr = int(input("Guess a number between 0 and 9: "))  # ask the user for a number
while user_nr != x and tries <= max_tries:  # check if the user guessed the number, if not ask for another number
    tries = tries + 1
    user_nr = int(input("You were wrong! Try again: "))

if tries > max_tries:
    print("You lost! The number was " + str(x))
else:
    print("You guessed it!")
