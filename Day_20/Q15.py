import functools

lst = ['54', '546', '548', '60']

def compare(str1, str2):
    str1str2=str1+str2
    str2str1=str2+str1
    return int(str1str2) - int(str2str1)

x = sorted(lst, key=functools.cmp_to_key(compare),reverse=True)
result = "".join(x)
print(result)