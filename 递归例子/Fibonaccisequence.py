import time


# 斐波那契数列

# 注意，这里的x表示位置，所以，在第一位和第二位时，都是1
def factorial(x):
    if x == 1 or x == 2:
        return 1
    else:
        return factorial(x - 1) + factorial(x - 2)


# 注意，这里的x表示位置，所以，在第一位和第二位时，都是1(x是不能为0的，在数学里面，位置是从1开始的)
def iteration(x):
    if x <= 2:
        return 1
    else:
        first = 1
        second = 1
        result = 1
        for i in range(2, x):
            result = first + second
            first = second
            second = result
    return result

t1 = time.time()
print(factorial(34))
print("factorial消耗时间：" + str(time.time() - t1))

t2 = time.time()
print(iteration(100000))
print("iteration消耗时间：" + str(time.time() - t2))


list = []
# 注意，这里的表示位置，但是for循环这里，下标从0开始
def getMathValue(x):
    for i in range(x):
        if i == 0 or i == 1:
            list.append(1)
        else:
            list.append(list[i - 2] + list[i - 1])
    return list



# print(getMathValue(30))

