a = [2, 2, 0, 4, 0, 8]
print("o",a)

count = 0
for i in range(len(a)-1):
    if(a[i+1] == a[i] and a[i] != 0):
        a[i] = 2*a[i+1]
        a[i+1] = 0
print(a)

for i in range(len(a)):
    if(a[i]!=0):
        a[i], a[count] = a[count], a[i]
        count += 1
print(a)
