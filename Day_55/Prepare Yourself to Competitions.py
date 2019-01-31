"""
Creater: Aman Ranjan Verma

"""

def prep(a, b):
    preparation= 0
    index = 0
    diff = []
    flag = 0
    for i in range(len(a)):
        index += [a[i], b[i]].index(max(a[i], b[i]))
        preparation += max(a[i], b[i])
        diff.append(abs(a[i]-b[i]))
        if(a[i] == b[i]):
            flag = 1
    if(flag == 0 and (index == 0 or index == len(a))):
        preparation = preparation - min(diff)
    return preparation


a = [1, 2]
b = [2, 1]
print(prep(a,b))