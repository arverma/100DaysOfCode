a = [12, 3, 5, 1, 7, 19]
k = 3

b = set()
b.add(0)
for i in a:
    b.add(i)
b.remove(0)

for i in range(len(b)-k-1):
    b.pop()
print('Kth Smallest Element is: ', b.pop())