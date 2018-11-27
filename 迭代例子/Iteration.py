# 递归和迭代的方式实现
# 题目：函数f由如下的规则定义：如果n < 3，那么f(n) = n；如果n >= 3，那么f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3)。请写一个采用递归计算过程计算f的过程。再写一个采用迭代计算过程计算f的过程。

def factorial(n):
    if (n < 3):
        f = n
    else:
        f = factorial(n - 1) + 2 * factorial(n - 2) + 3 * factorial(n - 3)
    return f


print(factorial(4))
