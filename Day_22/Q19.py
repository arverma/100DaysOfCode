a = [-12, 11, -13, -5, 6, -7, 5, -3, -6, 0]
n = len(a)
print(a, n-1)
index = n-1 #Just a variable
for i in range(n):
    if(a[i] >= 0 and i < index-1):
        while(a[index]>=0):
            index -= 1
        a[i], a[index] = a[index], a[i] #SWAP
    print(a,index)