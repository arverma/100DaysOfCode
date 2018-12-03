import heapq
import math as m

a = [8,7,6,5,4,3,2,1]
k = 3 

heapq.heapify(a) # In linear time O(n)
print("Heapified = ", a)

# For K Largest | Time = O(klog(n))
print("K Largest = ",sorted(a[len(a): m.floor(m.log2(k)):-1], reverse = True)[0:k])

# For K Smallest | Time = O(klog(n))
print("K Smallest = ",sorted(a[0:k]))






#----------------Code for max Heapify--------------------------
'''
import math as m 
a = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]

def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
    return A

def build_max_heap(A):
    for i in range((len(A) // 2)-1, -1, -1):
        A = max_heapify(A, i)
        print(A,i)
    return A
    
print(build_max_heap(a))

'''