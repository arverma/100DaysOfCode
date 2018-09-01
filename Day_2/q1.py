
n = int(input())
a= list(map(int, input (). split ()))

def most_common(lst):
    return max(set(lst), key=lst.count)

b = most_common(a)
c = [i for i, e in enumerate(a) if e == 1]
d = n - len(c)
print(d)