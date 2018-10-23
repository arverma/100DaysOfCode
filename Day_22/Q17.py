a = [ 1,2,3,4,5,6]
n = len(a)
b = []
b.extend(a)
max = n-1
min = 0
for i in range(n):
    if(i%2 == 0):
        a[i] = b[max]
        max -= 1 
    else:
        a[i] = b[min]
        min += 1
print(a)