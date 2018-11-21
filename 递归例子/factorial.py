def factorialMath(x):
    if x == 0 or x == 1:
        f = 1
    else:
        f = factorialMath(x - 1) * x
    return f
print(factorialMath(100))