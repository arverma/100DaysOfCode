a = [12, 11, -13, -5, 6, -7, 5, -3, -6]

for i in range(len(a)-1):
    if(a[i+1]<0):
        j = i
        key = a[i+1]
        # print(a,j,a[j])
        while(a[j]>0):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
print(a)
