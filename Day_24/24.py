a = [1, 2, 3, 4, 5, 6, 7, 8] 
n = len(a)

import random as r  
for i in range(n):
    temp = r.randint(0, n-1)
    a[temp], a[i] = a[i], a[temp]
    print(a)