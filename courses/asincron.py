import time


async def sync(x):
    time.sleep(3)
    print(x + 1)
    return x + 1


print('1')
y = sync(2)
print('2')
time.sleep(4)


