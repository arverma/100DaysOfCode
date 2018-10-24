a = [21, 3, 40, 5, 60]

n = len(a)
temp = a[0]
a[0] = a[0]*a[1]
for i in range(1, n):
    if(i == n-1):
        a[i] = a[i] * temp
    else:
        flag = temp
        temp = a[i]
        a[i] = flag * a[i+1]
        
print(a)
        