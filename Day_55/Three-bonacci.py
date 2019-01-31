"""
Creater: Aman Ranjan Verma

"""
def bonacci(a, b, c, n):
    if(n == 0):
        return a
    elif(n == 1):
        return b
    elif(n == 2):
        return c   
    return bonacci(a, b, c, n-1) + bonacci(a, b, c, n-2) + bonacci(a, b, c, n-3)

n = 10
print(bonacci(0, 1, 2, n))