
a = [54, 546, 548, 60, 600]
print(a)
#a.sort()
print(a)
a = list(map(str, a))
a = list(map(list, a))
print(a)

k = len(a[0])
#j = 0
l = 0
for i in range(len(a[len(a)-1])):
    j = 0
    while(len(a[j]) == k):
        j += 1
        print(j)
        if(j == len(a)):
            break
    a[l:len(a)] = sorted(a[l: len(a)], key=lambda b: b[i], reverse = True)
    print(l,i,a)
    l = j
    k += 1







