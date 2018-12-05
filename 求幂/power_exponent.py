import decimal
import math

from decimal import Decimal


def powerExpont(a, b):
    if a == 0:
        return 0
    if a == 1 or b == 0:
        return 1
    if b == 1:
        return a
    a0 = a
    for i in range(1,b):
        a0 = a0 * a
    return a0
def powerExpont2(a, b):
    if a == 0:
        return 0
    if a == 1 or b == 0:
        return 1
    if b == 1:
        return a
    a = decimal.Decimal(a)
    a0 = decimal.Decimal(a)
    for i in range(1,b):
        a0 = a0*a
    return a0

print(powerExpont(0.2,5))

print(math.pow(0.2,5))
print(0.2**5)
# 传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确
print(powerExpont2("0.2",5))
