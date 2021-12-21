import sys

args = sys.argv[1:]  # when we take args from the command line, we remove the first element (it is the file name)

strings = []
for x in args:
    if not x.isnumeric():  # isnumeric function will return True if there are only numbers in it
        strings.append(x)

strings = [x for x in args if not x.isnumeric()]

print(strings)
