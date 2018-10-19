a = [2, 4, 8, 0]
n = len(a)
a = a + a

def hamming(a,n):
    max = 0
    for i in range(n):
        hamm = 0
        print("i = ",i)
        for j in range(i,i+n):
            if(a[j]!=a[j+1]):
                print("hamm = ", hamm)
                hamm += 1
                if(hamm>max):
                    max = hamm
                elif(hamm == n):
                    return n
    return max
print(hamming(a,n))
            
        