arr = [2, 0, 1, 4, 5, 3]
print(arr)
# {1, 2, 0, 5, 3, 4}

# b = []
# b.extend(a)
# for i in range(len(a)):
#     a[b[i]] = i
# print(a)

n = len(arr)
for i in range(n):
    # print(arr[i], i)
    arr[arr[i] % n] += i * n
    print(arr)

for i in range(n):
    arr[i] //= n
print(arr)