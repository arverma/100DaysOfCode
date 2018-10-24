a = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]

n = len(a)

for i in range(n-1):
    if(i%2 == 0 and a[i] < 0):
        if(a[i+1] > 0):
            a[i], a[i+1] = a[i+1], a[i]
        elif(a[i-1] > 0 and i != 0):
            a[i], a[i-1] = a[i-1], a[i]
        pass
    elif(i%2 != 0 and a[i] > 0):
        if(a[i+1] < 0):
            a[i], a[i+1] = a[i+1], a[i]
        elif(a[i-1] < 0):
            a[i], a[i-1] = a[i-1], a[i]
        pass
    print(a)