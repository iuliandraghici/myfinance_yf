import math

x = math.ceil(5.78)
print(x)
x = math.floor(5.78)
print(x)

a = math.fabs(-5)
print(a)
a = math.fabs(5)
print(a)

f = math.factorial(19)
print(f)

cmmdc = math.gcd(27, 36)
print(cmmdc)

l = [1, 3, 5]
print(math.prod(l, start=0))

s = math.sqrt(4)
print(s)
s = math.pow(2, 2)
print(s)

print(math.pi)


def fibonacci(numar: int) -> list:
    s = [0, 1]
    while len(s) < numar:
        new_value = s[-1] + s[-2]
        s.append(new_value)
    return s


print(fibonacci(20))
