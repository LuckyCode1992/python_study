# 最大公约数，辗转相除法，欧几里得算法
# （16 6）-》16%6=4-》（6，4）-》6%4 = 2 -》（4，2）-》4%2=0  -》2是最大公约数
import sys


def bigCommonMeasure1(x, y):
    return y if (x % y == 0) else bigCommonMeasure1(y, x % y)

# 辗转相除法 缺点是，数字大了之后，栈的深度会很深，所以不建议使用
def bigCommonMeasure2(x, y):
    if x == y:
        return x
    if (abs(x - y)) > y:
        return bigCommonMeasure2(abs(x - y), y)
    else:
        return bigCommonMeasure2(y, abs(x - y))

print(bigCommonMeasure1(24, 18))
print(bigCommonMeasure2(24, 18))

