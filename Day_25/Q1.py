def partition(a, l, r):
    
    # The partition algorithm is taken from quicksort where the pivot 
    # element accupy the position such that all elements before it are 
    # less than pivot element and all elements after pivot are greater
    # that it.
    
    x = a[r]
    k = l-1
    for j in range(l, r):
        if(a[j] < x):
            k += 1
            a[k], a[j] = a[j], a[k]
    k += 1
    a[k], a[r] = a[r], a[k]
    return k

def selection(a, key, l, r):
    
    # We get the index of pivot element. Case:
    # if pivot = key-1 : we are done
    # if pivot > key-1 : recurse in lower side
    # if pivot < key-1 : recurse in upper side
    
    p = partition(a,l,r)
    
    print('partition = ',p)
    if(p-l == key-1):
        return a[p]
    elif(p-l > key-1):
        return selection(a, key, l, p-1)
    return selection(a, key-p+l-1 , p+1, r)
    

a = [12, 3, 5, 7, 4, 19, 26]
key = 3
n = len(a)
l = 0 
r = n-1
print('K\'th smallest element is ',selection(a, key, l, r))
print(a)