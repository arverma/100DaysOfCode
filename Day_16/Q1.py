def swap(arr,i,k):
    arr[i], arr[k] = arr[k], arr[i]
    return arr

def rearrange(arr, n):
    i = 0
    for j in range(n):
        if (arr[j] < 0):
            swap(arr,i,j)
            i += 1
    k = 0
    print(arr)
    
    while(arr[k] < 0 and k < n and i< n):
        arr  = swap(arr, k, i)
        i += 1
        k += 2
        
# A utility function to print an array 
def printArray(arr, n):
	for i in range(n): 
		print(arr[i], end= " ")

# Driver program to test above functions 
arr = [-5, -2, 5, 2, 4, 7, 1, 8, -8, 0] 
n = len(arr) 
print(arr)
rearrange(arr, n) 
printArray(arr, n) 

# Contributed by Afzal 
