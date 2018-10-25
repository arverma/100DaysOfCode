a = [1, 3, 2, 4, 7, 6, 9, 10 ] 
n = len(a)

index = 1
for i in range(n):
    if(a[i]%2 != 0):
        while(a[index]%2 != 0 and index< n-1):
            index += 1
        a[i], a[index] = a[index], a[i]
    print(a)
        