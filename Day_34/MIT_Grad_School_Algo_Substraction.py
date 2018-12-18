# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:30:27 2018

@author: amanranjan
"""
a = str(1234) # Always larger in size
b = str(34) #Always smaller in size

choice = input("Choice:\n1. a-b\n2. b-a\n")

a = list(map(int, a))
b = list(map(int, b))
a.reverse()
b.reverse()
result = []

for i in range(len(b)):
    if(b[i]>a[i]):
        a[i] = a[i] + 10
        a[i+1] -= 1 
        result.append(a[i]-b[i])
    else:
        result.append(a[i]-b[i])
        
result.extend(a[i+1::])
result.reverse()
result = ''.join(str(e) for e in result)
result = int(result)

if choice == "1":
    pass
elif choice == "2":
    result = -1*result
else:
    print("Please Enter Correct Choice.")
    result = "XXX"
    
print("Result = ", result)
    
