prime_no = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,83, 89, 97]

# Complexity = sqrt(n)
check = 87
 
if check>0:
    k = (check)**(1/2)
    if(k > round(k)):
        k = round(k) + 1
    else:
        k = round(k)
    print(k)

prime = [ i for i in prime_no if i<k]
flag = 1
for j in prime:
    if check%j==0:
        print(j)
        flag = 0
        break
    else:
        flag = 1

if flag == 0:
    print("Not Prime")
else:
    print("Prime")
        
    