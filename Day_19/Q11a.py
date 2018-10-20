# {1, 9, 2, 8, 3, 7, 4, 6, 5}
a = [5, 8, 1, 4, 2, 9, 3, 7, 6]
print(a)
for j in range(len(a)):
    if(j%2 == 0):
        for i in range(len(a)-1, j, -1):
            if(a[i-1]>a[i]):
                a[i], a[i-1] = a[i-1], a[i]
            # print(j,a)
    else:
        for i in range(len(a)-1, j, -1):
            if(a[i-1]<a[i]):
                a[i], a[i-1] = a[i-1], a[i]
    print(a)
    