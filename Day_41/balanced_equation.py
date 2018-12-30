"""

Check for a balanced equatrion
Balanced Equation: 
    1. the existance of '(' and ')' both
    2. the existance of '{' and '}' both

"""
def checkbalance(a):
    print(a)
    check_left = ['(', '{']
    check_right = [')', '}']
    stack = []
    n = -1
    for i in range(len(a)):
        print(a[i], stack, n, end = "")
        if(a[i] in check_left):
            print("L")
            stack.append(a[i])
            n += 1
        elif(a[i] in check_right):
            k = check_right.index(a[i])
            print("R", k)
            if(n >= 0 and stack[n]==check_left[k]):
                stack.pop()
                n -= 1
            else:
                return "Voilated at " + str(i+1)
        else:
            print("")
    if(len(stack)!=0):
        return "Not Balanced"
    return "Balanced"


expression = "".join("if a(4 > 9)) { foo(a(2)); }".split())

print(checkbalance(expression))