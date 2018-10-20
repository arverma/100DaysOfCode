# {1, 9, 2, 8, 3, 7, 4, 6, 5}
a = [5, 8, 1, 4, 2, 9, 3, 7, 6]
print("o",a)
a.sort()
b = []
b.extend(a)
print("s",b)
k = 0
i = 0
for j in range(len(a)):
    if(j % 2 == 0):
        a[j] = b[k]
        k +=1
        pass
    else:
        a[j] = b[len(a)-1-i]
        i += 1
        pass
print(a)