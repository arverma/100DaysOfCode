def findMin(arr, low, high):
    if high <= low: 
        return arr[high] 
    mid = int((low + high)/2) 
    if mid < high and arr[mid+1] < arr[mid]: 
        return arr[mid] 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return arr[mid-1] 
    if arr[low] < arr[mid]: 
        return findMin(arr, mid+1, high) 
    return findMin(arr, low, mid-1) 
  
# Driver program to test above functions 
arr1 = [5, 6, 1, 2, 3, 4] 
n1 = len(arr1) 
print("The minimum element is " + str(findMin(arr1, 0, n1-1))) 
  
arr2 = [1, 2, 3, 4] 
n2 = len(arr2) 
print("The minimum element is " + str(findMin(arr2, 0, n2-1))) 
  
arr3 = [1] 
n3 = len(arr3) 
print("The minimum element is " + str(findMin(arr3, 0, n3-1))) 
  
arr4 = [1, 2] 
n4 = len(arr4) 
print("The minimum element is " + str(findMin(arr4, 0, n4-1))) 
  
arr5 = [2, 1] 
n5 = len(arr5) 
print("The minimum element is " + str(findMin(arr5, 0, n5-1))) 
  
arr6 = [5, 6, 7, 1, 2, 3, 4] 
n6 = len(arr6) 
print("The minimum element is " + str(findMin(arr6, 0, n6-1))) 
  
arr7 = [1, 2, 3, 4, 5, 6, 7] 
n7 = len(arr7) 
print("The minimum element is " + str(findMin(arr7, 0, n7-1))) 
  
arr8 = [2, 3, 4, 5, 6, 7, 8, 1] 
n8 = len(arr8) 
print("The minimum element is " + str(findMin(arr8, 0, n8-1))) 
  
arr9 = [3, 4, 5, 1, 2] 
n9 = len(arr9) 
print("The minimum element is " + str(findMin(arr9, 0, n9-1))) 
  
# This code is contributed by Pratik Chhajer 