a = [1, 2, 3, 4, 5, 6, 7]
q = [[0, 4], [0, 6]]
pivot = 1
for i in q[::-1]: %% Reverse
    left = i[0]
    right = i[1]
    if(pivot >= i[0] and pivot <= i[1]):
        if(left == pivot ):
            pivot = right
        else:
            pivot -= pivot
print(a[pivot%len(a)])