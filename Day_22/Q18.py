a = [ 1,2,3,4,5,6,7]
n = len(a)
max = n-1
min = 0
for i in range(n):
    if(i%2 == 0):
        a[i] += a[max] % (n+1)*(n+1)
        max -= 1 
    else:
        a[i] += a[min] % (n+1)*(n+1)
        min += 1
for i in range(n):
    a[i] //= (n+1)
    
print(a)