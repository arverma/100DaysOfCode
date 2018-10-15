a = [7, 9, 10, 12, 1]
n = len(a)
while a[0] <= a[1]:
    a = a[1:n] + [a[0]]
a = a[1:n] + [a[0]]
if(a[0]<a[1] and a[1] < a[n-1]):
    print("YES")
else:
    print("NO")