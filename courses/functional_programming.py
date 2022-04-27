f = lambda x: x + 1

print(f(5))


def xplus1(l: list) -> list:
    return [x + 1 for x in l]

p = xplus1([5,6,7,8])
print(p)


def xplusn(n: int):
    return lambda x: x + 5

f = xplusn(5)
print(f(5))


