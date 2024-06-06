# Threaded Proxy Object

## pip install threadproxyobject

### Tested against Windows 10 / Python 3.11 / Anaconda


```PY
import pandas as pd
import random
from time import sleep
from threadedproxyobject import ThreadedProxyObject, ThreadedProxyObjectMultiExecute


def funct(x, y):
    return random.randint(x, y)


def funct2(x, y):
    return [x + y]


def funct3(x, y):
    while True:
        print(random.randint(x, y))
        sleep(1)


test = ThreadedProxyObject(funct, args=(1, 200))
test.start()
print(test)
sleep(1)
print((test) ** 10)

test2 = ThreadedProxyObject(funct2, args=(1, 200))
test2.start()
print((test2))
sleep(1)
test2.append(3)
print(test2)

test3 = ThreadedProxyObjectMultiExecute(fu=funct, args=(1, 200))
test3()
print((test3))
sleep(1)
print(test3 / 10)

test4 = ThreadedProxyObjectMultiExecute(fu=funct2, args=(1, 200))
test4()
sleep(1)
print(test4 * 10)

test5 = ThreadedProxyObjectMultiExecute(fu=funct3, args=(1, 200))
test5()
print((test5))
test5.kill()
test6 = ThreadedProxyObjectMultiExecute(fu=funct, daemon=False, args=(1, 200))
test6.start_timer_call(3)
sleep(4)
print((test6))
print(test6 + 10)
test6.stop_timer_call()


liste = [
    ThreadedProxyObjectMultiExecute(
        fu=funct, daemon=True, args=(1, 200)
    ).start_timer_call(3)
    for x in range(100)
]
sleep(2)
df = pd.DataFrame(liste)
print(df[0] * 2)

# 45
# 34050628916015625
# [201]
# [201, 3]
# 129
# 12.9
# [201, 201, 201, 201, 201, 201, 201, 201, 201, 201]
# 141
# N/A
# 151
# 161
# 0     128
# 1     314
# 2     220
# 3     102
# 4     220
#      ... 
# 95     72
# 96    314
# 97     24
# 98    144
# 99     24
# Name: 0, Length: 100, dtype: object

```