import math as m

def partition(a, l, r, x):
    temp = a.index(x)
    a[temp], a[r] = a[r], a[temp] # Swap it to put that element at last 

    k = l-1
    for j in range(l, r):
        if(a[j] < x): 
            k += 1
            a[k], a[j] = a[j], a[k]
    k += 1
    a[k], a[r] = a[r], a[k]
    return k

def kthSmallest(a,l,r,key):
    n = len(a)
    
    # Finding Median
    median = []
    for i in range(0, n, 5):
        if(i+5 < n):
            temp = sorted(a[i:i+5])
            median.append(a[m.floor((2*i+5)/2)])
        else:
            temp = sorted(a[i:n])
            median.append(a[m.floor((i+n-1)/2)])
    
    # Finding Median of median
    if len(median) == 1:
        medOfMed = median[0]
    else:
        medOfMed = kthSmallest(median, 0, len(median)-1, m.floor(len(median)/2))
    
    p = partition(a, l, r, medOfMed)
    if(p-l == key-1):
        return a[p]
    elif(p-l > key-1):
        return kthSmallest(a, l, p-1, key)
    return kthSmallest(a, p+1, r, key-p+l-1 )


#----------Driver-------------
a = [12, 3, 5, 7, 4, 19, 26]
l = 0
r = len(a)-1 
k = 3
print('kthSmallest = ', kthSmallest(a, l, r, k))

