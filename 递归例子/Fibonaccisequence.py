list = []
def getMathValue(x):
    for i in range(x):
        if i==0 or i==1:
            list.append(1)
        else:
            list.append(list[i-2]+list[i-1])
    return list
print(getMathValue(30))
