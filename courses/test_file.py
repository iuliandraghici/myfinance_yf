import os


def get_first_line(filename, mode):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            return file.readline()
    else:
        return None


line = get_first_line('yfinance_excel.py', 'w')

print(line)

print("What is your name?")
name = input()
print(name)
