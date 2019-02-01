"""
Creater: Aman Ranjan Verma

"""

def compare(a, b): 
    ab = str(a) + str(b) 
    ba = str(b) + str(a) 
    print((int(ba) > int(ab)) - (int(ba) < int(ab)))
    return (int(ba) > int(ab)) - (int(ba) < int(ab))
        
def largest(lst):
    import functools
    x = sorted(lst, key=functools.cmp_to_key(compare))
    result = "".join(map(str,x))
    if(int(result) == 0):
        result = "0"
    return result 
  
print(largest([1, 34, 3, 98, 9, 76, 45, 4]))