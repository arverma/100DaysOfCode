# 40, 60, 90, 50, 70

a = [10, 11, 12]
# print(a)
b = [1, 0, 2]

for i in range(len(a)):
    if( i >= b[i] ):
        a[i], a[b[i]] = a[b[i]], a[i]
print(a)
        