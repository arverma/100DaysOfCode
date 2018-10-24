a = [2, 3, 4, 5]
n = len(a)

for i in range(n-1):
    if(i % 2 == 0 and a[i]>a[i+1]):
        a[i], a[i+1] = a[i+1], a[i]
        pass
    elif(i % 2 != 0 and a[i]<a[i+1]):
        a[i], a[i+1] = a[i+1], a[i]
        pass
    print(a)