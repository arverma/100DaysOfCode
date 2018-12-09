#------------ Complexity = O(k*n) -----------------

a = [[10, 20, 30, 40],[15, 25, 35, 45],[24, 29, 37, 48], \
    [32, 33, 39, 50]]

# print(a)
n_row = len(a)

def kth_smallest(a, k, key):
    temp = []
    for i in range(n_row): # List of Column 1 
        temp.append(a[i][0])
        
    # print(temp)
    small = temp[0]
    flag = 0
    for i in range(n_row): # Finding smallest from that row
        if(temp[i]<=small):
            small = temp[i]
            flag = i
    # print('flag = ', flag)
    #Swap the smallest and an element from that row  
    a[flag][0], a[flag][key[flag]] = a[flag][key[flag]], a[0][flag]
    key[flag] += 1

    # print(small, flag, key)
    print(small)
    # print(a)
    
    if(k > 0): # Do it for 'k' times
        kth_smallest(a, k-1, key)

k = 7
key = {0:1, 1:1, 2:1, 3:1}
print(kth_smallest(a, k, key))