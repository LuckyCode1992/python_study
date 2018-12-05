# 递归方法求值
#  第0层 1
#  第1层 1
#  第2层 k=0 -》1  k=2 ->1
#  第3层 k=0 ->1  k=3 ->1
#   -》 n == k ->1 n==0 n==1->1
#                 1
#               1   1
#              1  2  1     2: n=2,k=1   （n-1,k-1）+(n-1,k)
#             1 3  3  1     3: n = 3,k = 1   (n-1,k-1)+(n-1,k)
#            1 4  6  4  1
import numpy as np


def factorial(n, k):
    if n < k:
        return 'n不能小于k'
    if k == 0:
        return 1
    if n == 0:
        return 1
    if n == k:
        return 1
    return factorial(n - 1, k - 1) + factorial(n - 1, k)


print(factorial(8, 2))


# 迭代法，求帕斯卡三角形某个位置得值

def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        # N = [
        #     N[i - 1] + N[i]
        #      for i in range(len(N))
        #      ]
        for i in range(len(N)):
            N[i] = N[i-1]+N[i]
m = 0
for t in triangles():
    print(t)
    m = m + 1
    if m == 20:
        break
# print(iteration(6, 2))
